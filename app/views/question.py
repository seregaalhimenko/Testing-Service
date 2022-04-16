from app.models import Question
from app.serializers import QuestionSerializer as Serializer
from app.castom_permission import AuthorOrReadOnly
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = Serializer
    permission_classes = [AuthorOrReadOnly]