# for ProtectionError using
from django.db import models

from rest_framework import serializers
from api.models import Poll, Question

class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'id',
            'title', 
            'start_date',
            'end_date',
            'description'
        ]
    
    def update(self, instance, validated_data):
        """Перед сохранением экземпляра бросить исключение
        при попытке изменить readonly-поле.

        По задаче: у опроса после создания нельзя изменять start_date
        """
        if instance.start_date != validated_data.get('start_date', instance.start_date):
            raise models.ProtectedError("Нельзя изменять поле 'start_date'", None)
        else:
            return serializers.HyperlinkedModelSerializer.update(self, instance, validated_data)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = [
            'poll_id',
            'question_text'
        ]