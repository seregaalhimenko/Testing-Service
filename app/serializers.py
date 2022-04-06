# from django.conf import settings
# from rest_framework import serializers
# from app import models


# class ThemeSerializer(serializers.ModelSerializer):
#     ''' Theme model serializer '''
#     class Meta:
#         model = models.Theme
#         fields = "__all__"


# class TestListSerializer(serializers.ModelSerializer):
#     ''' Theme model serializer '''
#     class Meta:
#         model = models.Test
#         fields = ['id', 'name', '']

# class ThemeDetailSerializer(serializers.ModelSerializer):
#     ''' Theme model serializer '''
#     test_set =TestListSerializer(many=True, read_only=True, required=False)
#     class Meta:
#         model = models.Theme
#         fields = ['name', 'theory','test_set']


# #----------------------------------------------------------------------------------

# class ChoiceShowSerializer(serializers.ModelSerializer):
#     ''' Choice model serializer '''
#     class Meta:
#         model = models.Choice
#         fields = ['id', 'text']

# class QuestionShowSerializer(serializers.ModelSerializer):
#     ''' Question model serializer '''
#     choice_set = ChoiceShowSerializer(many=True, read_only=True, required=False)
#     class Meta:
#         model = models.Question
#         fields = "__all__"
