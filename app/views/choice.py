from app.models import Choice
from app.serializers import ChoiceSerializer as Serializer
from rest_framework import mixins
from rest_framework import generics
from app.castom_permission import AuthorOrReadOnly


class ChoiceCR(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Choice.objects.all()
    serializer_class = Serializer
    permission_classes = [AuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ChoiceURD(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Choice.objects.all()
    serializer_class = Serializer
    permission_classes = [AuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
