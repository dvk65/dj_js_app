import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #pub_date = models.DateTimeField('date publilshed')
    #title_key=models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
