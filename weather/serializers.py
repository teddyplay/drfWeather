from rest_framework import serializers
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
    # фунция  для вывода сыррого формата json
    print(json)









    # class Meta:
    #     model = Stars
    #     fields = ('title', 'content', 'cat_id')

