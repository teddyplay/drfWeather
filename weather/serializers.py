from rest_framework import serializers

from .models import Stars


class StarsModel:
    def __init__(self, title , content):
        self.title = title
        self.content = content
        # модель для преобразования в json формат



class StarsSerializer(serializers.Serializer): # будем брать из бд модели






    # class Meta:
    #     model = Stars
    #     fields = ('title', 'content', 'cat_id')

