from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=250, default="", null=True, blank=True)
    password = models.CharField(max_length=500, default="", null=True, blank=True)
    email = models.CharField(max_length=250, default="", null=True, blank=True)
    Aadharnumber = models.CharField(max_length=100, default="", null=True, blank=True)
    User_type =  models.CharField(max_length=100, default="", null=True, blank=True)
    CreatedBy = models.BooleanField(default=False, null=False, blank=False)
    CreatedDate = models.DateTimeField(null=True)
    UpdatedBy = models.IntegerField(null=True)
    UpdatedDate = models.DateTimeField(null=True)
    DeletedBy = models.IntegerField(null=True)
    DeletedDate = models.DateTimeField(null=True)


class Account_Detils(models.Model):
    username = models.CharField(max_length=250, default="", null=True, blank=True)
    user_id = models.CharField(max_length=250, default="", null=True, blank=True)
    cripto_amount = models.CharField(max_length=100, default="", null=True, blank=True)
    CreatedDate = models.DateTimeField(null=True)


class chat_messagers(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate messages with users
    messages = models.TextField()
    user_name = models.CharField()
    times = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.time}"