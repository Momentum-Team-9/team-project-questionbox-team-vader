from django.contrib.auth.models import User
from core.models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    #author = serializers.SerializerMethodField()
    
    #author = serializers.SlugRelatedField(read_only=False, slug_field="username")
    class Meta:
        model = Question
        fields = ('pk', 'question', 'created_date', 'author')
        
    # def get_author(self,obj):
    #     return str(obj.author_id.username)
        
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'answer', 'created_date', 'author', 'question', 'accepted')