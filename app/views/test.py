from app.models import Test
from app.serializers import TestSerializer as Serializer
from app.castom_permission import AuthorOrReadOnly
from rest_framework import viewsets

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = Serializer
    permission_classes = [AuthorOrReadOnly]