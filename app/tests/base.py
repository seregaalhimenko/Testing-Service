from rest_framework.test import APITestCase
from app.models import *
from django.contrib.auth import get_user_model

from django.db.models import Model
from rest_framework.serializers import Serializer


class BaseTestCase(APITestCase):

    def setUp(self) -> None:
        data = {"email": "Test@test.com", "password": "Test1234!"}
        self.client.post("http://0.0.0.0:8000/auth/users/",
                         data, format='json')
        self.user_test = get_user_model().objects.get(email='Test@test.com')
        self.client.force_authenticate(user=self.user_test)

        self.theme = Theme(name="Test_theme", theory="Test_theory")
        self.theme.save()
        self.test = Test(author=self.user_test, name="tests", theme=self.theme)
        self.test.save()
        self.question = Question(
            author=self.user_test, text="test_question", test=self.test)
        self.question.save()

        self.choice1 = Choice(author=self.user_test,
                              text="Yes", value=True, questions=self.question)
        self.choice1.save()
        self.choice2 = Choice(author=self.user_test, text="No",
                              value=False, questions=self.question, comment="comment")
        self.choice2.save()
        self.user2 = get_user_model().objects.create(
            email="answ1@test.com", password="Test1234!")
        self.user3 = get_user_model().objects.create(
            email="answ2@test.com", password="Test1234!")
        # self.answer1 = AnswerTracker(
        #     user=self.user3, test=self.test, question=self.question, choice=self.choice2)
        # self.answer1.save()
        # self.answer2 = AnswerTracker(
        #     user=self.user2, test=self.test, question=self.question, choice=self.choice1)
        # self.answer2.save()

        self.url_datail = None
        self.url_list = None
        self.serializer: Serializer = None
        self.model: Model = None
