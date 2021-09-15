from django.contrib.auth.models import User
from core.models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'question', 'created_date', 'author')