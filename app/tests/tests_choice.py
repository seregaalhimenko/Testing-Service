import json
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from app.models import Choice
from app.serializers import ChoiceSerializer

from django.db.models import Model
from rest_framework.serializers import Serializer
from app.tests.base import BaseTestCase


class Tests(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.point = self.choice2
        self.url_datail = reverse('choice-detail', kwargs={
            'pk': self.point.id})
        self.url_list = reverse('choice-list')
        self.serializer: Serializer = ChoiceSerializer
        self.model: Model = Choice

    def test_create(self):
        """
        Ensure we can create a new Question object.
        """

        url = self.url_list
        data = {
            'author': self.user_test.id,
            "text": "choicenew",
            "value": False,
            "questions": self.question.id,
            "comment": "bad"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.model.objects.get(
            id=response.data['id']).text, 'choicenew')

    def test_show(self):
        url = self.url_datail
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = self.serializer(self.point).data
        self.assertEqual(data, json.loads(response.content))
        url = self.url_list
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(data, json.loads(response.content))

    def test_update(self):
        url = self.url_datail
        data = {
            "text": "choice_update"
        }
        response: Response = self.client.patch(
            url,
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        obj = self.model.objects.get(id=self.point.id)
        obj_ser = self.serializer(obj)
        self.assertEqual(
            json.loads(response.content)["text"], obj_ser.data["text"])

    def test_delete(self):
        url = self.url_datail
        response: Response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
