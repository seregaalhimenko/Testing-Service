from app.models import Test
from app.result_serializers import ResultSerializer
from rest_framework.response import Response
from rest_framework import generics
from app.castom_permission import AuthorOrReadOnly


class Result (generics.GenericAPIView):
    queryset = Test.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        test= self.queryset.get(id = kwargs["test_id"])
        return Response(data=ResultSerializer(test).data)