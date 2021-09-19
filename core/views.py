from django.http import JsonResponse

from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionListViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    # def perform_create(self, serializer):         
    #     question = Question.objects.get(pk=self.kwargs.get('question_pk'))         
    #     if self.request.user is not question.user:             
    #         raise PermissionDenied()         
    #     serializer.save(question=question)

class QuestionDetailsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
def AnswersForQuestions(request, pk):
    question = get_object_or_404(Question, pk = pk)
    output = []
    
    for answer in question.answers.all():
        output.append(AnswerSerializer(answer).data)
    return JsonResponse({'answers': output})