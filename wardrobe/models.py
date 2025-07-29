from django.db import models
from django.contrib.auth.models import User


class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    image = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


