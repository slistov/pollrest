from rest_framework import serializers
from api.models import Poll, Question

class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'title', 
            'start_date',
            'end_date',
            'description'
        ]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = [
            'poll_id',
            'question_text',
            'answer_type'
        ]