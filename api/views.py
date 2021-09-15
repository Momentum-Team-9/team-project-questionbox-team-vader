from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from core.models import Question
from .serializers import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer