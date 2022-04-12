import json

from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from app.models import Question
from app.serializers import QuestionSerializer

from django.db.models import Model
from rest_framework.serializers import Serializer
from app.tests.base import BaseTestCase


class Tests(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.url_datail = reverse('question_detail', kwargs={
            'pk': self.question.id})
        self.url_list = reverse('question_list')
        self.serializer: Serializer = QuestionSerializer
        self.model: Model = Question

    def test_create(self):
        """
        Ensure we can create a new Question object.
        """

        url = self.url_list
        data = {
            'author': self.user_test.id,
            "text": "question",
            "test": self.test.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.model.objects.get(
            id=response.data['id']).text, 'question')

    def test_show(self):
        url = self.url_datail
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = self.serializer(self.question).data
        self.assertEqual(data, json.loads(response.content))
        url = self.url_list
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(data, json.loads(response.content))

    def test_update(self):
        id = self.question.id
        url = self.url_datail
        data = {
            'author': self.user_test.id,
            "text": "question_update",
            "test": self.test.id
        }

        response: Response = self.client.put(
            url,
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        obj = self.model.objects.get(id=id)
        obj_ser = self.serializer(obj)
        self.assertEqual(
            json.loads(response.content), obj_ser.data)

    def test_delete(self):
        url = self.url_datail
        response: Response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
