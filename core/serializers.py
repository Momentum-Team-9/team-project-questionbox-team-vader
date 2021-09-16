from django.contrib.auth.models import User
from core.models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model = Question
        fields = ('pk', 'question', 'created_date', 'author')
        
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'answer', 'created_date', 'author', 'question', 'accepted')