from attr import field
from django.conf import settings
from rest_framework import serializers
from app import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    ''' User model serializer '''
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = "__all__"


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    ''' Theme model serializer '''
    class Meta:
        model = models.Theme
        fields = '__all__'


class TestSerializer(serializers.HyperlinkedModelSerializer):
    ''' Test model serializer '''
    class Meta:
        model = models.Test
        fields = "__all__"


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    ''' Question model serializer '''
    class Meta:
        model = models.Question
        fields = "__all__"


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    ''' Choice model serializer '''
    class Meta:
        model = models.Choice
        fields = "__all__"


class ResaltSerializer(serializers.HyperlinkedModelSerializer):
    ''' AnswerTracker model serializer '''
    class Meta:
        model = models.AnswerTracker
        fields = "__all__"


