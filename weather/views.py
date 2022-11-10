from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics #базовый класс для предсавленя drf
from rest_framework.response import Response
from weather.models import Stars
from weather.serializers import StarsSerializer
from rest_framework.views import APIView




class StarsAPIView(APIView):
    def get(self, request):
        s = Stars.objects.all()
        return Response({'posts': StarsSerializer(s, many=True).data})   # Возращать клиенту json стороку,

    def post(self, request):
        serializer = StarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # проверка на провалильновать введных данных
        serializer.save() # автоматом добавляет новую запись, берет с serailizers


        # new_post = Stars.objects.create( # создаю функцию создания поста
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        # )
        return Response({'post': serializer.data})







# class StarsAPIView(generics.ListAPIView):
#     queryset = Stars.objects.all() # будет брать все поля модели
#     serializer_class = StarsSerializer




