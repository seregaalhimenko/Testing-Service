from django.urls import path
# from app import api
from app.views import theme, test, question, answer_tracker, choice


urlpatterns = [
    path('theme/', theme.ThemeCR.as_view(), name="theme_list"),
    path('theme/<int:pk>/', theme.ThemeURD.as_view(), name="theme_detail"),
    # path('theme/<int:id_theme>/test/<int:id_test>/question/<int:id_question>/',views.TestStartView.as_view()),
    path('test/', test.TestCR.as_view()),
    path('test/<int:pk>/', test.TestURD.as_view()),
    path('question/', question.QuestionCR.as_view()),
    path('question/<int:pk>/', question.QuestionURD.as_view()),
    path('choice/', choice.ChoiceCR.as_view),
    path('choice/<int:pk>/', choice.ChoiceURD.as_view()),
    path('result/', answer_tracker.AnswerTrackerCR.as_view()),
    path('result/<int:pk>/', answer_tracker.AnswerTrackerURD.as_view()),

]
