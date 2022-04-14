from django.conf import settings
from rest_framework import serializers
from app import models

class ChoiceSerializer(serializers.ModelSerializer):
    ''' Choice model serializer '''
    class Meta:
        model = models.Choice
        fields = ['id', 'text']

class AnswerSerializer(serializers.ModelSerializer):
    text= serializers.CharField(source='choice.text')
    value= serializers.CharField(source='choice.value')
    comment= serializers.CharField(source='choice.comment', allow_null=True)
    class Meta:
       model = models.AnswerTracker
       fields = ['text', 'value', 'comment']

class QuestionSerializer(serializers.ModelSerializer):
    ''' Question model serializer '''
    choice_set = ChoiceSerializer(
        many=True, read_only=True, required=False)
    answertracker_set = AnswerSerializer(
        many=True, read_only=True, required=False)
    class Meta:
        model = models.Question
        # fields = ['id', 'text', 'choice_set', 'answer_set']
        fields = "__all__"

class ResaltSerializer(serializers.ModelSerializer):
    ''' Test model serializer '''
    question_set = QuestionSerializer(
        many=True, read_only=True, required=False)

    class Meta:
        model = models.Test
        fields = ['id', 'name', 'question_set']
