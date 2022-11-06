from django.shortcuts import render
from rest_framework import generics #базовый класс для предсавленя drf

from weather.models import Stars


class StarsAPIView(generics.ListAPIView):
    queryset = Stars.objects.all() # будет брать все поля модели
    serializer_class = StarsSerializers()

