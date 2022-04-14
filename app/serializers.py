from django.conf import settings
from rest_framework import serializers
from app import models


class ChoiceSerializer(serializers.ModelSerializer):
    ''' Choice model serializer '''
    class Meta:
        model = models.Choice
        fields = ['id', 'author', 'text', 'value', 'questions', 'comment']


class QuestionSerializer(serializers.ModelSerializer): 
    ''' Question model serializer '''
    class Meta:
        model = models.Question
        fields = ['id', 'author', 'text', 'test']


class ChoiceShowSerializer(serializers.ModelSerializer):
    ''' Choice model serializer '''
    class Meta:
        model = models.Choice
        fields = ['id', 'text']



class QuestionShowSerializer(serializers.ModelSerializer):
    ''' Question model serializer '''
    choice_set = ChoiceShowSerializer(
        many=True, read_only=True, required=False)

    class Meta:
        model = models.Question
        fields = ['id', 'author', 'text', 'test', 'choice_set']


class QuestionShortSerializer(serializers.ModelSerializer):
    ''' Question model serializer '''
    class Meta:
        model = models.Question
        fields = ['id']

class TestShortListSerializer(serializers.ModelSerializer):
    ''' Test model serializer '''
    question_set = QuestionShortSerializer(
        many=True, read_only=True, required=False)

    class Meta:
        model = models.Test
        fields = ['id', 'question_set']



class TestSerializer(serializers.ModelSerializer):
    ''' Test model serializer '''
    # question_set = QuestionDetailSerializer(
    #     many=True, read_only=True, required=False)

    class Meta:
        model = models.Test
        fields = ['id', 'author', 'name', 'theme']


class ThemeSerializer(serializers.ModelSerializer):
    ''' Theme model serializer '''
    # test_set = TestDetailSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = models.Theme
        fields = ['id', 'name', 'theory']

class InAnswerTrackerSerializer(serializers.ModelSerializer):
    ''' AnswerTracker model serializer '''
    class Meta:
        model = models.AnswerTracker
        fields = ['user', 'test', 'question', 'choice']
        

class AnswerTrackerSerializer(serializers.ModelSerializer):
    ''' AnswerTracker model serializer '''
    class Meta:
        model = models.AnswerTracker
        fields = ['id', 'user', 'test', 'question', 'choice']
