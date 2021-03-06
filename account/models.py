from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    man=1
    woman=2
    status_choices=((man, 'مرد'),(woman, 'زن'))

    gender=models.IntegerField(choices=status_choices)
    profile=models.ImageField(upload_to='profile/')
