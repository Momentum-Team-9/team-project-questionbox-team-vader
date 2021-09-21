from rest_framework.permissions import IsAuthenticated
from core.permissions import IsQuestionOwnerOrReadOnly

from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Answer, User, Question
from .serializers import AnswerSerializer, ProfileListSerializer, QuestionDetailSerializer, QuestionListSerializer


class QuestionListViewSet(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    
class UserQuestionListViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileListSerializer
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(username=self.request.user)
    
    def get_queryset(self):
        queryset = self.queryset.filter(username=self.request.user)
        return queryset
    
        
class QuestionDetailsViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsQuestionOwnerOrReadOnly]
    
    
class AddAnswerViewSet(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)