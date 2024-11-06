from django.db import models
from django.db.models import IntegerField
from django.forms import CharField

# Create your models here.
class book(models.Model):
    book_name=models.CharField(max_length=1000)
    book_author=models.CharField(max_length=1000)
    book_age=models.IntegerField()

