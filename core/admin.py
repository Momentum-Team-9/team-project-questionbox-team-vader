from django.contrib import admin
from .models import User, Question

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_date', 'author']
