from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(db_index=True, unique=True)
    mobileNumber = models.CharField(null=True,max_length=18, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=255)
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE, default=None, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
