from api.serializers import PollSerializer, QuestionSerializer
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import Poll, Question

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all().order_by('-start_date')
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    