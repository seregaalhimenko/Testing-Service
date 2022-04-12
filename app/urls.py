from django.urls import path
# from app import api
from app.views import theme, test, question, answer_tracker, choice, views


urlpatterns = [
    path('theme/', theme.ThemeCR.as_view(), name="theme_list"),
    path('theme/<int:pk>/', theme.ThemeURD.as_view(), name="theme_detail"),
    # path('start-app/',views.StartQuiz.as_view()),
    path('start-app/<int:test_id>/',views.StartQuiz.as_view(), name="start_app"),
    path('test/', test.TestCR.as_view(), name="test_list"),
    path('test/<int:pk>/', test.TestURD.as_view(), name="test_detail"),
    path('question/', question.QuestionCR.as_view(), name="question_list"),
    path('question/<int:pk>/', question.QuestionURD.as_view(),
         name="question_detail"),
    path('choice/', choice.ChoiceCR.as_view(), name="choice_list"),
    path('choice/<int:pk>/', choice.ChoiceURD.as_view(), name="choice_detail"),
    path('result/', answer_tracker.AnswerTrackerCR.as_view(), name="result_list"),
    path('result/<int:pk>/', answer_tracker.AnswerTrackerURD.as_view(), name="result_detail"),

]
