from django.db import models


# Create your models here.
class ItemSettings(models.Model):
    section = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    showhide = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    beam = models.CharField(max_length=100)

    def __str__(self):
        return str(self.section)
