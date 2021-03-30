from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.


class ProfileModel(models.Model): # ORM
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f"profile_images", blank=True)
    created_time = models.DateTimeField(auto_now_add=datetime.now())
    timestamp = models.DateTimeField(auto_now=datetime.now(), blank=True)
    # testing_field = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.user.username} created at {self.created_time.year}-{self.created_time.month}-" \
               f"{self.created_time.day}"
