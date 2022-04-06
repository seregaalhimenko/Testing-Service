from django.conf import settings
from rest_framework import serializers
from app import models


class UserDetailSerializer(serializers.ModelSerializer):
    ''' User model serializer '''
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = "__all__"


class ChoiceDetailSerializer(serializers.ModelSerializer):
    ''' Choice model serializer '''
    class Meta:
        model = models.Choice
        fields = "__all__"


class QuestionDetailSerializer(serializers.ModelSerializer):
    ''' Question model serializer '''
    choice_set = ChoiceDetailSerializer(
        many=True, read_only=True, required=False)

    class Meta:
        model = models.Question
        fields = "__all__"


class TestDetailSerializer(serializers.ModelSerializer):
    ''' Test model serializer '''
    question_set = QuestionDetailSerializer(
        many=True, read_only=True, required=False)

    class Meta:
        model = models.Test
        fields = "__all__"


class ThemeDetailSerializer(serializers.ModelSerializer):
    ''' Theme model serializer '''
    test_set = TestDetailSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = models.Theme
        fields = '__all__'


class AnswerTrackerDetailSerializer(serializers.ModelSerializer):
    ''' AnswerTracker model serializer '''
    class Meta:
        model = models.AnswerTracker
        fields = "__all__"
