from app.models import Theme
from app.serializers import ThemeSerializer as Serializer
from rest_framework import viewsets


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = Serializer
    tags = ["Theme"]
