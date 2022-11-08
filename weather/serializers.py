import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Stars


class StarsModel:
    def __init__(self, title , content):
        self.title = title
        self.content = content
        # модель для преобразования в json формат



class StarsSerializer(serializers.Serializer): # будем брать из бд модели
    title = serializers.CharField(max_length=350)
    content = serializers.CharField()


def encode():
    model = StarsModel('Rick and Morty', 'content: rick and morty')
    model_sr = StarsSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)
    # фунция  для вывода сыррого формата json


def decode():
    stream = io.BytesIO(b'{"title":"tick and morty", "content":"Content: Rick and Morty"}')
    data = JSONParser().parse(stream)
    serializers = StarsSerializer(data=data)
    serializers.is_valid()
    print(serializers.validated_data)
#функция для получения сырых данных json






    # class Meta:
    #     model = Stars
    #     fields = ('title', 'content', 'cat_id')

