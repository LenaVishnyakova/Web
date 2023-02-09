from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    header = models.CharField(max_length=100)
    note_text = models.TextField()
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.header
