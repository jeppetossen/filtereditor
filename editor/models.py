from django.db import models


# Create your models here.
class FilterSettings(models.Model):
    section = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    beam = models.CharField(max_length=100)

    def __str__(self):
        return self.section
