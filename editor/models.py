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
    # item_level = models.CharField(max_length=100)
    # drop_level = models.CharField(max_length=100)
    # quality = models.CharField(max_length=100)
    item_class = models.CharField(max_length=100)
    base_type = models.CharField(max_length=100)
    # sockets = models.CharField(max_length=100)
    # sockets_linked = models.CharField(max_length=100)
    socket_group = models.CharField(max_length=100)
    # height = models.CharField(max_length=100)
    # width = models.CharField(max_length=100)
    # gem_level = models.CharField(max_length=100)
    identified = models.CharField(max_length=100)
    corrupted = models.CharField(max_length=100)
    elder_item = models.CharField(max_length=100)
    shaper_item = models.CharField(max_length=100)
    shaped_map = models.CharField(max_length=100)
    # map_tier = models.CharField(max_length=100)
    # border_color = models.CharField(max_length=100)
    # text_color = models.CharField(max_length=100)
    # background_color = models.CharField(max_length=100)
    font_size = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)
    # icon = models.CharField(max_length=100)
    # beam = models.CharField(max_length=100)

    def __str__(self):
        return self.section, self.subsection, self.block, \
               self.show_hide, self.rarity, self.sound, \
               self.icon, self.beam
