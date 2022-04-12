# Create your tests here.
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from app.models import Theme
from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient
from app.serializers import ThemeSerializer
# response = self.client.post("http://0.0.0.0:8000/auth/token/login/", data, format='json')
# token = response.data["auth_token"]


class ThemeTests(APITestCase):

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

    def test_create_Theme(self):
        """
        Ensure we can create a new Theme object.
        """
        response = self.create_theme()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Theme.objects.count(), 1)
        # response.headers["Location"] по договоренности rest (вроде) id созданной модели должен быть в location и не должен возвращать нечего...поправим :)
        self.assertEqual(Theme.objects.get().name, 'test_theme')
        self.theme_id = response.data['id']

    def test_show_Theme(self):
        create_theme_response = self.create_theme()
        url = reverse('theme_detail', kwargs={
                      'pk': create_theme_response.data['id']})
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = ThemeSerializer(Theme.objects.get(
            id=create_theme_response.data['id'])).data
        self.assertEqual(data, json.loads(response.content))
        url = reverse('theme_list')
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(data, json.loads(response.content))

    def test_update_Theme(self):
        create_theme_response = self.create_theme()

        url = reverse('theme_detail', kwargs={
                      'pk': create_theme_response.data['id']})

        response: Response = self.client.put(
            url,
            {'name': 'test_theme_update', "theory": "test_theory_update"},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        obj = Theme.objects.get(id=create_theme_response.data['id'])
        obj_ser = ThemeSerializer(obj)

        self.assertEqual(
            json.loads(response.content), obj_ser.data)

    def test_delete_Theme(self):
        create_theme_response = self.create_theme()
        url = reverse('theme_detail', kwargs={
                      'pk': create_theme_response.data['id']})
        response: Response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
