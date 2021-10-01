# for ProtectionError using
from django.db import models

from rest_framework import serializers
from api.models import Poll, Question

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'id',
            'title', 
            'start_date',
            'end_date',
            'description'
        ]
        extra_kwargs = {
            'title': {'required': False},
            'start_date': {'required': False},
            'end_date': {'required': False},
            'description': {'required': False}
        }
        validators = []
    
    def update(self, instance, validated_data):
        """Исключение при попытке изменить readonly-поле.

        По задаче: у опроса после создания нельзя изменять start_date
        """
        if instance.start_date != validated_data.get('start_date', instance.start_date):
            raise models.ProtectedError("Нельзя изменять поле 'start_date'", None)
        else:
            # Вызвать метод родителя
            return serializers.ModelSerializer.update(self, instance, validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'poll_id',
            'question_text'
        ]