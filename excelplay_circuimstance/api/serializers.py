from rest_framework import serializers
from .models import (
    Level,
    CircuimstanceUser,
    Hint
)
from django.forms.fields import FileField


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Hint


class LevelSerializer(serializers.ModelSerializer):
    file = FileField()
    hints = HintSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'level',
            'level_file',
            'source_hint',
            'filetype',
            'hints',
        )
        model = Level


class CircuimstanceUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'user_id',
            'level',
            'rank',
        )
        model = CircuimstanceUser
