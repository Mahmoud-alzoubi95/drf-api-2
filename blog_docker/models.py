from django.contrib.auth import get_user_model
from django.db import models

class Glass(models.Model):
    Name = models.CharField(max_length=64)
    Discription = models.TextField()
    Admine = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
