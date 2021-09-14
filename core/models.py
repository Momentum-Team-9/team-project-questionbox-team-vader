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
        User, on_delete=models.CASCADE, related_name='questions', null=True)
    
    def __str__(self):
        return f"{self.question}"
