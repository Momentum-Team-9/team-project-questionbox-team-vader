from rest_framework.viewsets import ModelViewSet
from .models import Question
from .serializers import QuestionSerializer

class QuestionListViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
class QuestionDetailsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
