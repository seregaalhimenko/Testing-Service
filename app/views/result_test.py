from app.models import Test
from app.result_serializers import ResultSerializer
from rest_framework.response import Response
from rest_framework import generics
from app.castom_permission import AuthorOrReadOnly


class Result (generics.GenericAPIView):
    queryset = Test.objects.all()
    permission_classes = [AuthorOrReadOnly]
    serializer_class = ResultSerializer
    lookup_field = 'test_id'
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data=serializer.data)
