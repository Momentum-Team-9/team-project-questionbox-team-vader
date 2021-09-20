from core.models import Question, Answer
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Answer
        fields = ('pk', 'answer', 'created_date', 'author', 'question', 'accepted')

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only = True, default = serializers.CurrentUserDefault())

    class Meta:
        model = Question
        fields = ('pk', 'question', 'details', 'created_date', 'author', 'bookmark', 'answers')
        
        
class QuestionDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ('pk', 'question', 'details', 'created_date', 'author', 'bookmark', 'answers')
    
    
class QuestionListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Question
        fields = ('pk', 'question', 'created_date', 'author')