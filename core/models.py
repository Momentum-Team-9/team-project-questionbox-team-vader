from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import date

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
    
class Question(models.Model):
    question = models.CharField(max_length=250)
    created_date = models.DateField(default=date.today)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='questions', null=True)
    bookmark = models.ManyToManyField(User, related_name='bookmarked_question', blank=True)
    
    def __str__(self):
        return f"{self.question}"
    

class Answer(models.Model):
    answer = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='answer', null=True)
    created_date = models.DateField(default=date.today)
    question = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='answers', null=True)
    accepted = models.BooleanField(default=False)
    bookmark = models.ManyToManyField(User, related_name='bookmarked_answers', blank=True)

    def __str__(self):
        return f"{self.answer}"