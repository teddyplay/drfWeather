from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics #базовый класс для предсавленя drf
from rest_framework.response import Response
from weather.models import Stars
from weather.serializers import StarsSerializer
from rest_framework.views import APIView




class StarsAPIView(APIView):
    def get(self, request):
        lst = Stars.objects.all().values()
        return Response({'posts':list(lst)})   # Возращать клиенту json стороку,

    def post(self, request):
        new_post = Stars.objects.create( # создаю функцию создания поста
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(new_post)})



# class StarsAPIView(generics.ListAPIView):
#     queryset = Stars.objects.all() # будет брать все поля модели
#     serializer_class = StarsSerializer




