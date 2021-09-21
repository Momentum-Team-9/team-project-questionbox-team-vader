from core.models import Question, Answer, User
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Answer
        fields = ('pk', 'answer', 'created_date', 'author', 'question', 'accepted')
        
        
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
        
        
class ProfileListSerializer(serializers.ModelSerializer):
    questions = QuestionListSerializer(many=True, read_only=True)
    answer = AnswerSerializer(many=True, read_only=True)
    bookmarked_question = serializers.SlugRelatedField(many=True, queryset=Question.objects.all(), slug_field='question')
    bookmarked_answers = serializers.SlugRelatedField(many=True, queryset=Answer.objects.all(), slug_field='answer')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'questions', 'answer', 'bookmarked_question', 'bookmarked_answers')