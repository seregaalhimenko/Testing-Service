from app.models import Choice
from app.serializers import ChoiceSerializer as Serializer
from app.castom_permission import AuthorOrReadOnly
from rest_framework import viewsets


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = Serializer
    permission_classes = [AuthorOrReadOnly]