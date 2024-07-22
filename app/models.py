from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class raiseticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=150)

    def __str__(self) -> str:
        return self.title + ">>>"