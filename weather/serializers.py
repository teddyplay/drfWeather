from rest_framework import serializers

from .models import Stars


class StarsSerializer(serializers.ModelSerializer): # будем брать из бд модели
    class Meta:
        model = Stars
        fields = ('title', 'category')

