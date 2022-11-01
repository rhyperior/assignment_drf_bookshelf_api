from enum import unique
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

class Bookshelf(models.Model):
    name = models.CharField(max_length=80, unique=True)
    author = models.CharField(max_length=80)
    isbn_number = models.IntegerField(unique=True)
    publication = models.CharField(max_length=80, null=True)
    genre = models.CharField(max_length=50, null=True, blank=True)