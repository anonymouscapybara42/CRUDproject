from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    country = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name