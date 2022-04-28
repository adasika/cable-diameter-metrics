from dataclasses import field
from rest_framework import serializers
from .models import Cable


class Cable_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cable
        fields = ['time_stamp', 'minimum', 'average', 'maximum']
        