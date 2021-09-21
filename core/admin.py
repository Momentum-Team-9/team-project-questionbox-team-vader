from django.contrib import admin
from .models import User, Question, Answer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_date', 'author',]
    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'answer', 'question', 'created_date', 'author',]
