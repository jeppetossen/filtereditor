from django.db import models


# Create your models here.
class Section(models.Model):
    section = models.CharField(max_length=100, null=True, default=None)

    def __str__(self):
        return self.section


class SubSection(models.Model):
    subsection = models.CharField(max_length=100, null=True, default=None)
    section = models.OneToOneField(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsection


# Conditions
class ItemLevel(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    level = models.PositiveSmallIntegerField()


class DropLevel(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    level = models.PositiveSmallIntegerField()


class Quality(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    quality = models.PositiveSmallIntegerField()


class Rarity(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    rarity = models.CharField(max_length=100)


class Sockets(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    sockets = models.PositiveSmallIntegerField()


class LinkedSockets(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    links = models.PositiveSmallIntegerField()


class Height(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    value = models.PositiveSmallIntegerField()


class Width(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    value = models.PositiveSmallIntegerField()


class StackSize(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    value = models.PositiveSmallIntegerField()


class GemLevel(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    value = models.PositiveSmallIntegerField()


class MapTier(models.Model):
    operator = models.CharField(max_length=100, null=True, default=None)
    value = models.PositiveSmallIntegerField()


# Actions
class SetBorderColor(models.Model):
    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()
    alpha = models.PositiveSmallIntegerField(default=255)

    def __str__(self):
        return [self.red, self.green, self.blue, self.alpha]


class SetTextColor(models.Model):
    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()
    alpha = models.PositiveSmallIntegerField(default=255)

    def __str__(self):
        return [self.red, self.green, self.blue, self.alpha]


class SetBackgroundColor(models.Model):
    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()
    alpha = models.PositiveSmallIntegerField(default=255)

    def __str__(self):
        return [self.red, self.green, self.blue, self.alpha]


class PlayAlertSound(models.Model):
    sound_id = models.PositiveSmallIntegerField()
    volume = models.PositiveSmallIntegerField()


class PlayAlertSoundPositional(models.Model):
    sound_id = models.PositiveSmallIntegerField()
    volume = models.PositiveSmallIntegerField()


class MinimapIcon(models.Model):
    size = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=100, null=True, default=None)
    shape = models.CharField(max_length=100, null=True, default=None)


class BeamEffect(models.Model):
    color = models.CharField(max_length=100, null=True, default=None)
    temp = models.BooleanField(default=None)


class Block(models.Model):
    '''section = models.OneToOneField(Section, on_delete=models.CASCADE, null=True, default=None)
    subsection = models.OneToOneField(SubSection, on_delete=models.CASCADE, null=True, default=None)
    block = models.CharField(max_length=100, null=True, default=None)
    show_hide = models.CharField(max_length=100, null=True, default=None)
    item_class = models.CharField(max_length=100, null=True, default=None)
    base_type = models.CharField(max_length=100, null=True, default=None)
    rarity = models.OneToOneField(Rarity, on_delete=models.CASCADE, null=True, default=None)
    item_level = models.OneToOneField(ItemLevel, on_delete=models.CASCADE, null=True, default=None)
    drop_level = models.OneToOneField(DropLevel, on_delete=models.CASCADE, null=True, default=None)
    quality = models.OneToOneField(Quality, on_delete=models.CASCADE, null=True, default=None)
    sockets = models.OneToOneField(Sockets, on_delete=models.CASCADE, null=True, default=None)
    sockets_linked = models.OneToOneField(LinkedSockets, on_delete=models.CASCADE, null=True, default=None)
    socket_group = models.CharField(max_length=100, null=True, default=None)
    height = models.OneToOneField(Height, on_delete=models.CASCADE, null=True, default=None)
    width = models.OneToOneField(Width, on_delete=models.CASCADE, null=True, default=None)
    stack_size = models.OneToOneField(StackSize, on_delete=models.CASCADE, null=True, default=None)
    gem_level = models.OneToOneField(GemLevel, on_delete=models.CASCADE, null=True, default=None)
    identified = models.BooleanField(null=True, default=None)
    corrupted = models.BooleanField(null=True, default=None)
    elder_item = models.BooleanField(null=True, default=None)
    shaper_item = models.BooleanField(null=True, default=None)
    shaped_map = models.BooleanField(null=True, default=None)
    map_tier = models.OneToOneField(MapTier, on_delete=models.CASCADE, null=True, default=None)
    border_color = models.OneToOneField(SetBorderColor, on_delete=models.CASCADE, null=True, default=None)
    text_color = models.OneToOneField(SetTextColor, on_delete=models.CASCADE, null=True, default=None)
    background_color = models.OneToOneField(SetBackgroundColor, on_delete=models.CASCADE, null=True, default=None)
    font_size = models.PositiveSmallIntegerField(default=32)
    sound = models.OneToOneField(PlayAlertSound, on_delete=models.CASCADE, null=True, default=None)
    sound_pos = models.OneToOneField(PlayAlertSoundPositional, on_delete=models.CASCADE, null=True, default=None)
    icon = models.OneToOneField(MinimapIcon, on_delete=models.CASCADE, null=True, default=None)
    beam = models.OneToOneField(PlayEffect, on_delete=models.CASCADE, null=True, default=None)'''

    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, default=None)
    subsection = models.ForeignKey(SubSection, on_delete=models.CASCADE, null=True, default=None)
    block = models.CharField(max_length=100, null=True, default=None)
    show_hide = models.CharField(max_length=100, null=True, default=None)
    item_class = models.CharField(max_length=100, null=True, default=None)
    base_type = models.CharField(max_length=100, null=True, default=None)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE, null=True, default=None)
    item_level = models.ForeignKey(ItemLevel, on_delete=models.CASCADE, null=True, default=None)
    drop_level = models.ForeignKey(DropLevel, on_delete=models.CASCADE, null=True, default=None)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE, null=True, default=None)
    sockets = models.ForeignKey(Sockets, on_delete=models.CASCADE, null=True, default=None)
    sockets_linked = models.ForeignKey(LinkedSockets, on_delete=models.CASCADE, null=True, default=None)
    socket_group = models.CharField(max_length=100, null=True, default=None)
    height = models.ForeignKey(Height, on_delete=models.CASCADE, null=True, default=None)
    width = models.ForeignKey(Width, on_delete=models.CASCADE, null=True, default=None)
    stack_size = models.ForeignKey(StackSize, on_delete=models.CASCADE, null=True, default=None)
    gem_level = models.ForeignKey(GemLevel, on_delete=models.CASCADE, null=True, default=None)
    identified = models.BooleanField(null=True, default=None)
    corrupted = models.BooleanField(null=True, default=None)
    elder_item = models.BooleanField(null=True, default=None)
    shaper_item = models.BooleanField(null=True, default=None)
    shaped_map = models.BooleanField(null=True, default=None)
    map_tier = models.ForeignKey(MapTier, on_delete=models.CASCADE, null=True, default=None)
    border_color = models.ForeignKey(SetBorderColor, on_delete=models.CASCADE, null=True, default=None)
    text_color = models.ForeignKey(SetTextColor, on_delete=models.CASCADE, null=True, default=None)
    background_color = models.ForeignKey(SetBackgroundColor, on_delete=models.CASCADE, null=True, default=None)
    font_size = models.PositiveSmallIntegerField(default=32)
    sound = models.ForeignKey(PlayAlertSound, on_delete=models.CASCADE, null=True, default=None)
    sound_pos = models.ForeignKey(PlayAlertSoundPositional, on_delete=models.CASCADE, null=True, default=None)
    icon = models.ForeignKey(MinimapIcon, on_delete=models.CASCADE, null=True, default=None)
    beam = models.ForeignKey(BeamEffect, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.block
