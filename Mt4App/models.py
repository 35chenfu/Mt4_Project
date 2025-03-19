# Create your models here.
from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title