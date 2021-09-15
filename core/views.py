from rest_framework.viewsets import ModelViewSet
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

class QuestionListViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer