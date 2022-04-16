from app.models import Test, PassedTests, Question
from rest_framework import status
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from rest_framework.response import Response
from app.serializers import QuestionShowSerializer,InAnswerTrackerSerializer, TestShortListSerializer
from app.validators import request_is_valid
from django.shortcuts import get_object_or_404
  
def start_quiz(*,request: HttpRequest, pk: int)->Response:
    test_obj = get_object_or_404(Test,id=pk)
    ser_test = TestShortListSerializer(test_obj)
    if PassedTests.objects.filter(user=request.user).all():
        return  Response(status=status.HTTP_400_BAD_REQUEST,data={"error": "the user has already passed this test"})
    if 'results' not in request.session:
        request.session['results'] = list()
    if 'questions_arr' not in request.session:
        request.session['questions_arr'] = ser_test.data['question_set']

    if 'selected_question' in request.session:
        if not (request_is_valid(data=request.data, question_id=request.session['selected_question'].get('id'))):
            question_obj = Question.objects.get(id=request.session['selected_question'].get('id'))
            ser_question = QuestionShowSerializer(question_obj)
            return Response(status=status.HTTP_400_BAD_REQUEST,data={"error": "invalid response format",**ser_question.data})
        for answ in request.data:
            request.session['results'].append(
                {
                    "question":request.session['selected_question'].get('id'),
                    "user": request.user.id,
                    "test": pk,
                    "choice":answ,
                    }
                )

    if not len(request.session['questions_arr']):
        results = InAnswerTrackerSerializer(data=request.session['results'], many=True)
        if results.is_valid():
            results.save()
            PassedTests(user=request.user,test=get_object_or_404(Test,id=pk)).save()

        del request.session['questions_arr']
        del request.session['results']
        del request.session['selected_question']
        return HttpResponseRedirect(reverse("test-result_test",kwargs={"pk":pk}))
            
    
    request.session['selected_question'] = request.session['questions_arr'].pop()
    request.session.modified = True

    question_obj = get_object_or_404(Question, id=request.session['selected_question'].get('id'))
    ser_question = QuestionShowSerializer(question_obj)
    return Response(data=ser_question.data)