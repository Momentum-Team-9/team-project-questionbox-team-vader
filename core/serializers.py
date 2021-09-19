from core.models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only = True, default = serializers.CurrentUserDefault())
    answers = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('pk', 'question', 'created_date', 'author', 'answers')
    # def save(self):
    #     print('hello there')
    #     author =  self.context['request'].user
    #     print('general '+ str(author))
    #     question = self.validated_data['question']
    def get_answers(self):
        dir(self)
        print(dir(self))
        
                
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'answer', 'created_date', 'author', 'question', 'accepted')