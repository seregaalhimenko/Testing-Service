from app.models import AnswerTracker
from app.serializers import AnswerTrackerSerializer as Serializer
from rest_framework import permissions
from rest_framework import viewsets


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = AnswerTracker.objects.all()
    serializer_class = Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    tags = ["Answer"]
