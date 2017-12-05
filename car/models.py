from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=30)
    sn = models.CharField(max_length=30)
    last_accessed = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
