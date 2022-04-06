# from cgi import test
# from pyexpat import model
# from re import T
# from secrets import choice
# from rest_framework import generics, status
# from rest_framework.views import APIView, Response, Request
# from app import serializers
# from app import models
# from rest_framework import serializers as rest_serializers


# class ThemeListView(generics.ListAPIView):
#     queryset = models.Theme.objects.all()
#     serializer_class = serializers.ThemeListSerializer


# class ThemeDetailView(APIView):
#     def get(self, request: Request, pk):
#         theme = models.Theme.objects.get(id=pk)
#         serializer = serializers.ThemeDetailSerializer(theme)
#         return Response(serializer.data)

#     # def post(self,request: Request, pk):
#     #     test_id = request.data.get('id')
#     #     test = models.Test.objects.get(id = test_id)
#     #     serializer = serializers.TestDetailSerializer(test)
#     #     return Response(serializer)

# # class TestStartView(APIView):
# #     def get(self,_, **kwargs):

# #         # theme = models.Theme.objects.get(id=kwargs["id_theme"])#first vmesto get
# #         theme_id_from_url = kwargs["id_theme"]
# #         test =  models.Test.objects.get(id=kwargs["id_test"])
# #         theme_id_from_tets = test.id
# #         if theme_id_from_tets != theme_id_from_url:
# #             Response(status=status.HTTP_400_BAD_REQUEST)
# #         serializer = serializers.TestListSerializer(test)
# #         return Response()


# class TestStartView(APIView):
#     def get(self, _, **kwargs):
#         question = models.Question.objects.get(id=kwargs["id_question"])
#         test = models.Test.objects.get(question=question)
#         theme = models.Theme.objects.get(test=test)
#         if not(test.id == kwargs["id_test"] and theme.id == kwargs["id_theme"]):
#             return Response({'Bad Request': "invalid url"}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = serializers.QuestionShowSerializer(question)
#         return Response(serializer.data)
