from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from app.models import Test
from app.serializers import TestSerializer as Serializer
from app.castom_permission import AuthorOrReadOnly
from app.source import start_quiz
from app.result_serializers import ResultSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = Serializer
    permission_classes = [AuthorOrReadOnly]
    tags = ["Test"]

    @action(methods=['post'], detail=True, permission_classes=[permissions.IsAuthenticated],
            url_path='start', url_name='start_test')
    def start_quiz(self, request, pk, *args, **kwargs):
        return start_quiz(request=request, pk=pk)

    @action(methods=['get'], detail=True, permission_classes=[permissions.IsAuthenticated],
            url_path='result', url_name='result_test')
    def result(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        serializer_obj = ResultSerializer(instance)
        return Response(data=serializer_obj.data)
