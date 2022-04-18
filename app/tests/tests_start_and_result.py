import random as rd

from app.models import *
from app.serializers import QuestionShowSerializer
from app.tests.base import BaseTestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response


class Tests(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.q1 = Question(author=self.user_test,
                           text="test_question2", test=self.test)
        self.q1.save()
        self.q2 = Question(author=self.user_test,
                           text="test_question3", test=self.test)
        self.q2.save()
        self.choice1_q1 = Choice(author=self.user_test,
                                 text="answer1", value=True, questions=self.q1)
        self.choice2_q1 = Choice(author=self.user_test,
                                 text="answer2", value=False, questions=self.q1)
        self.choice3_q1 = Choice(author=self.user_test,
                                 text="answer3", value=True, questions=self.q1)
        self.choice4_q1 = Choice(author=self.user_test,
                                 text="answer4", value=False, questions=self.q1)
        self.choice1_q1.save()
        self.choice2_q1.save()
        self.choice3_q1.save()
        self.choice4_q1.save()

        self.choice1_q2 = Choice(author=self.user_test,
                                 text="answer1", value=True, questions=self.q2)
        self.choice2_q2 = Choice(author=self.user_test,
                                 text="answer2", value=False, questions=self.q2)
        self.choice3_q2 = Choice(author=self.user_test,
                                 text="answer3", value=True, questions=self.q2)
        self.choice4_q2 = Choice(author=self.user_test,
                                 text="answer4", value=False, questions=self.q2)
        self.choice1_q2.save()
        self.choice2_q2.save()
        self.choice3_q2.save()
        self.choice4_q2.save()

        self.url_start = reverse('test-start_test', kwargs={
            'pk': self.test.id})

    def set_random_answers(self, question_obj) -> list[int]:
        choice_set = question_obj.choice_set.values('id')
        answers_set = [i["id"] for i in choice_set]
        N = rd.randint(1, len(answers_set)-1)
        for _ in range(N):
            answers_set.remove(rd.choice(answers_set))
        return answers_set

    def castom_response_valid(self, response):
        self.assertIn('id', response.data)
        self.assertIn('author', response.data)
        self.assertIn('text', response.data)
        self.assertIn('choice_set', response.data)
        question_obj = Question.objects.get(id=response.data['id'])
        ser_obj = QuestionShowSerializer(question_obj)
        self.assertEqual(response.data, ser_obj.data)
        return self.set_random_answers(question_obj)

    def test_start(self):
        N = Question.objects.filter(test=self.test).count()
        response: Response
        answer = None
        results: dict = dict()
        for i in range(N):
            response = self.client.post(
                self.url_start, answer, content_type="application/json")
            answer = self.castom_response_valid(response)
            results[response.data['id']] = answer
        response = self.client.post(
            self.url_start, answer, content_type="application/json")
        self.assertRedirects(response, f"/app/test/{self.test.id}/result/", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        return results

    def test_double_start(self):
        self.test_start()
        answer = None
        response = self.client.post(
            self.url_start, answer, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {'error': 'the user has already passed this test'})

    def test_resalt(self):
        results = self.test_start()
        response = self.client.get(
            reverse("test-result_test", kwargs={"pk": self.test.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for key, value in results.items():
            for obj in response.data["question_set"]:
                if obj['id'] == key:
                    response_answers = [i["text"]
                                        for i in obj["answertracker_set"]]
                    db_answers = [Choice.objects.get(id=id).text
                                  for id in value]
                    self.assertListEqual(db_answers, response_answers)
