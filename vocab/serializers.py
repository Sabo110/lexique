from rest_framework import serializers
from .models import Mot


class MotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mot
        fields = '__all__'