from django.shortcuts import render
from rest_framework import generics #базовый класс для предсавленя drf
from rest_framework.response import Response

from weather.models import Stars
from weather.serializers import StarsSerializer
from rest_framework.views import APIView




class StarsAPIView(APIView):
    def get(self, request):
        return Response({'title':'Jason'})   # Возращать клиенту json стороку

# class StarsAPIView(generics.ListAPIView):
#     queryset = Stars.objects.all() # будет брать все поля модели
#     serializer_class = StarsSerializer

