from app.models import Theme
from app.detail_serializers import ThemeDetailSerializer as Serializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
# Такой метод добавляет лишние эндпоинты в свагер
# class BaseCRUD(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                mixins.RetrieveModelMixin,
#                mixins.UpdateModelMixin,
#                mixins.DestroyModelMixin,
#                generics.GenericAPIView):
#               pass


# class ThemeCRUD(BaseCRUD):

#     queryset = Theme.objects.all()
#     serializer_class = Serializer

#     def get(self, request, *args, **kwargs):
#         if kwargs.get("pk",None):
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


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
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
