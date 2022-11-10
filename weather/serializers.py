import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Stars


# class StarsModel:в
#     def __init__(self, title , content):
#         self.title = title
#         self.content = content
        # модель для преобразования в json формат



class StarsSerializer(serializers.Serializer): # будем брать из бд модели
    title = serializers.CharField(max_length=350)
    content = serializers.CharField()
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
    # class Meta:
    #     model = Stars
    #     fields = ('title', 'content', 'cat_id')

    def create(self, validated_data):
        return Stars.objects.create(**validated_data) # позволяет создаватвь новые посты

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', validated_data.content)
        instance.is_published = validated_data.get('is_published', validated_data.is_published)
        instance.cat_id = validated_data.get('cat_id', validated_data.cat_id)
        instance.save()
        return instance # метод для изменения данных - объекта








# def encode():
#     model = StarsModel('Rick and Morty', 'content: rick and morty')
#     model_sr = StarsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#     # фунция  для вывода сыррого формата json
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"tick and morty", "content":"Content: Rick and Morty"}')
#     data = JSONParser().parse(stream)
#     serializers = StarsSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)
#функция для получения сырых данных json








