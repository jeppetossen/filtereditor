from django.db import models


# Create your models here.
class ItemSection(models.Model):
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.section


class ItemSubSection(models.Model):
    subsection = models.CharField(max_length=100)
    section = models.OneToOneField(ItemSection, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsection


class ItemSettings(models.Model):
    section = models.OneToOneField(ItemSection, on_delete=models.CASCADE, null=True, default=None)
    subsection = models.OneToOneField(ItemSubSection, on_delete=models.CASCADE, null=True, default=None)
    block = models.CharField(max_length=100)
    show_hide = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    beam = models.CharField(max_length=100)

    def __str__(self):
        return self.section, self.subsection, self.block, \
               self.show_hide, self.rarity, self.sound, \
               self.icon, self.beam
