import json
from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from app.models import Test
from django.contrib.auth import get_user_model
from app.serializers import TestSerializer


class Tests(APITestCase):

    def setUp(self) -> None:
        data = {"email": "Test@test.com", "password": "Test1234!"}
        self.client.post("http://0.0.0.0:8000/auth/users/",
                         data, format='json')
        self.user_test = get_user_model().objects.get(email='Test@test.com')
        self.client.force_authenticate(user=self.user_test)

    def create_theme(self) -> Response:
        url = reverse('theme_list')
        data = {'name': 'test_theme', "theory": "test_theory"}
        return self.client.post(url, data, format='json')

    def create_test(self) -> Response:
        response = self.create_theme()
        url = reverse('test_list')
        data = {
            'author': self.user_test.id,
            "name": "tetsTests",
            "theme": response.data['id']
        }
        return self.client.post(url, data, format='json')

    def test_create_Test(self):
        """
        Ensure we can create a new Test object.
        """
        response = self.create_test()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Test.objects.count(), 1)
        self.assertEqual(Test.objects.get().name, 'tetsTests')
        self.test_id = response.data['id']

    def test_show_Test(self):
        create_test_response = self.create_test()
        url = reverse('test_detail', kwargs={
                      'pk': create_test_response.data['id']})
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = TestSerializer(Test.objects.get(
            id=create_test_response.data['id'])).data
        self.assertEqual(data, json.loads(response.content))
        url = reverse('test_list')
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(data, json.loads(response.content))

    def test_update_Test(self):
        create_test_response = self.create_test()

        url = reverse('test_detail', kwargs={
                      'pk': create_test_response.data['id']})

        data = {
            'author': self.user_test.id,
            "name": "tetsTests",
            "theme": create_test_response.data['id']
        }

        response: Response = self.client.put(
            url,
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        obj = Test.objects.get(id=create_test_response.data['id'])
        obj_ser = TestSerializer(obj)

        self.assertEqual(
            json.loads(response.content), obj_ser.data)

    def test_delete_Test(self):
        create_test_response = self.create_test()
        url = reverse('test_detail', kwargs={
                      'pk': create_test_response.data['id']})
        response: Response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
