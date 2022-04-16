from django.urls import path, include, re_path
# from app import api
from app.routers import routers
from app.views import test, question, answer_tracker, choice, views, result_test


urlpatterns = [
    path('', include(routers.router.urls)),
    path('start-app/<int:test_id>/',views.StartQuiz.as_view(), name="start_app"),
    path('result/<int:test_id>/', result_test.Result.as_view(), name="result_test"),


]
