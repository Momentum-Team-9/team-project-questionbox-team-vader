from rest_framework.viewsets import ModelViewSet
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import PermissionDenied
class QuestionListViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
# class QuestionAddViewSet(CreateAPIView):     
#     queryset = Question.objects.all()     
#     serializer_class = QuestionSerializer 

#     def perform_create(self, serializer):         
#         question = Question.objects.get(pk=self.kwargs.get('question_pk'))         
#         if self.request.user is not question.user:             
#             raise PermissionDenied()         
#         serializer.save(question=question)