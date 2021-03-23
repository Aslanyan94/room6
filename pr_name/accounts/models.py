from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.


class ProfileModel(models.Model): # ORM
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="")
    created_time = models.DateTimeField(auto_now_add=datetime.now())