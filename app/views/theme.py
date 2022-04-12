from app.models import Theme
from app.serializers import ThemeSerializer as Serializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions


class ThemeCR(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Theme.objects.all()
    serializer_class = Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ThemeURD(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):

    queryset = Theme.objects.all()
    serializer_class = Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
