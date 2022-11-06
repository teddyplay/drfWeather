from django.shortcuts import render
from rest_framework import generics #базовый класс для предсавленя drf

from weather.models import Stars
from .serializers import StarsSerializer


class StarsAPIView(generics.ListAPIView):
    queryset = Stars.objects.all() # будет брать все поля модели
    serializer_class = StarsSerializer()

