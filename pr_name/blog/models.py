from django.db import models
from accounts.models import User
from datetime import datetime
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=datetime)

    def __str__(self):
        return self.title

