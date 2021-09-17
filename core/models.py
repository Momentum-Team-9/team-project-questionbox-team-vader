from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import date

class User(AbstractUser):
    # def create_user(self, email, password):
    #     """
    #     Creates and saves a User with the given email, date of
    #     birth and password.
    #     """
    #     if not email:
    #         raise ValueError('Users must have an email address')

    #     user=self.model(
    #         email=self.normalize_email(email),
    #     )

    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    
    # USER_CREATE_PASSWORD_RETYPE=True
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['first_name','last_name', 'email']

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
    
class Question(models.Model):
    question = models.CharField(max_length=250)
    details = models.TextField(null=True, blank=True)
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