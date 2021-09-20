from core.permissions import IsQuestionOwnerOrReadOnly
from django.http import JsonResponse

from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import PermissionDenied

from .models import Question, Answer
from .serializers import QuestionDetailSerializer, QuestionSerializer, AnswerSerializer, QuestionListSerializer


class QuestionListViewSet(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

class QuestionDetailsViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsQuestionOwnerOrReadOnly]
    

class AnswerListViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def question_detail(request, pk):
        question = get_object_or_404(Question, pk = pk)
        output = QuestionSerializer(question).data

        answers = []
        for answer in question.answers.all():
            answers.append(AnswerSerializer(answer).data)
        output['answers'] = answers

        return JsonResponse(output)