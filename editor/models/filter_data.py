from django.db import models


class FilterSection(models.Model):
    filter_section = models.CharField(max_length=100, null=True, default=None)

    def __unicode__(self):
        return self.filter_section


class FilterSubSection(models.Model):
    filter_subsection = models.CharField(max_length=100, null=True, default=None)
    filter_section = models.ForeignKey(FilterSection, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.filter_subsection


# Conditions
class FilterItemLevel(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_level = models.PositiveSmallIntegerField(null=True, default=None)

    def __unicode__(self):
        return self


class FilterDropLevel(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_level = models.PositiveSmallIntegerField(null=True, default=None)

    def __unicode__(self):
        return self


class FilterQuality(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_quality = models.PositiveSmallIntegerField(null=True, default=None)


class FilterRarity(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_rarity = models.CharField(max_length=100, null=True, default=None)


class FilterSockets(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_sockets = models.PositiveSmallIntegerField(null=True, default=None)


class FilterLinkedSockets(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_links = models.PositiveSmallIntegerField(null=True, default=None)


class FilterHeight(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_value = models.PositiveSmallIntegerField(null=True, default=None)


class FilterWidth(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_value = models.PositiveSmallIntegerField(null=True, default=None)


class FilterStackSize(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_value = models.PositiveSmallIntegerField(null=True, default=None)


class FilterGemLevel(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_value = models.PositiveSmallIntegerField(null=True, default=None)


class FilterMapTier(models.Model):
    filter_operator = models.CharField(max_length=100, null=True, default=None)
    filter_value = models.PositiveSmallIntegerField(null=True, default=None)


# Actions
class FilterSetBorderColor(models.Model):
    filter_red = models.PositiveSmallIntegerField(null=True, default=None)
    filter_green = models.PositiveSmallIntegerField(null=True, default=None)
    filter_blue = models.PositiveSmallIntegerField(null=True, default=None)
    filter_alpha = models.PositiveSmallIntegerField(default=255)

    def __unicode__(self):
        return [self.filter_red, self.filter_green, self.filter_blue, self.filter_alpha]


class FilterSetTextColor(models.Model):
    filter_red = models.PositiveSmallIntegerField(null=True, default=None)
    filter_green = models.PositiveSmallIntegerField(null=True, default=None)
    filter_blue = models.PositiveSmallIntegerField(null=True, default=None)
    filter_alpha = models.PositiveSmallIntegerField(default=255)

    def __unicode__(self):
        return [self.filter_red, self.filter_green, self.filter_blue, self.filter_alpha]


class FilterSetBackgroundColor(models.Model):
    filter_red = models.PositiveSmallIntegerField(null=True, default=None)
    filter_green = models.PositiveSmallIntegerField(null=True, default=None)
    filter_blue = models.PositiveSmallIntegerField(null=True, default=None)
    filter_alpha = models.PositiveSmallIntegerField(default=255)

    def __unicode__(self):
        return [self.filter_red, self.filter_green, self.filter_blue, self.filter_alpha]


class FilterPlayAlertSound(models.Model):
    filter_sound_id = models.PositiveSmallIntegerField(null=True, default=None)
    filter_volume = models.PositiveSmallIntegerField(null=True, default=None)


class FilterPlayAlertSoundPositional(models.Model):
    filter_sound_id = models.PositiveSmallIntegerField(null=True, default=None)
    filter_volume = models.PositiveSmallIntegerField(null=True, default=None)


class FilterMinimapIcon(models.Model):
    filter_size = models.PositiveSmallIntegerField()
    filter_color = models.CharField(max_length=100, null=True, default=None)
    filter_shape = models.CharField(max_length=100, null=True, default=None)


class FilterBeamEffect(models.Model):
    filter_color = models.CharField(max_length=100, null=True, default=None)
    filter_temp = models.BooleanField(null=True, default=None)


class FilterBlock(models.Model):
    filter_section = models.ForeignKey(FilterSection, on_delete=models.CASCADE, null=True, default=None)
    filter_subsection = models.ForeignKey(FilterSubSection, on_delete=models.CASCADE, null=True, default=None)
    filter_block = models.CharField(max_length=100, null=True, default=None)
    filter_show_hide = models.CharField(max_length=100, null=True, default=None)
    filter_item_class = models.CharField(max_length=100, null=True, default=None)
    filter_base_type = models.CharField(max_length=100, null=True, default=None)
    filter_rarity = models.ForeignKey(FilterRarity, on_delete=models.CASCADE, null=True, default=None)
    filter_item_level = models.ForeignKey(FilterItemLevel, on_delete=models.CASCADE, null=True, default=None)
    filter_drop_level = models.ForeignKey(FilterDropLevel, on_delete=models.CASCADE, null=True, default=None)
    filter_quality = models.ForeignKey(FilterQuality, on_delete=models.CASCADE, null=True, default=None)
    filter_sockets = models.ForeignKey(FilterSockets, on_delete=models.CASCADE, null=True, default=None)
    filter_sockets_linked = models.ForeignKey(FilterLinkedSockets, on_delete=models.CASCADE, null=True, default=None)
    filter_socket_group = models.CharField(max_length=100, null=True, default=None)
    filter_height = models.ForeignKey(FilterHeight, on_delete=models.CASCADE, null=True, default=None)
    filter_width = models.ForeignKey(FilterWidth, on_delete=models.CASCADE, null=True, default=None)
    filter_stack_size = models.ForeignKey(FilterStackSize, on_delete=models.CASCADE, null=True, default=None)
    filter_gem_level = models.ForeignKey(FilterGemLevel, on_delete=models.CASCADE, null=True, default=None)
    filter_identified = models.BooleanField(null=True, default=None)
    filter_corrupted = models.BooleanField(null=True, default=None)
    filter_elder_item = models.BooleanField(null=True, default=None)
    filter_shaper_item = models.BooleanField(null=True, default=None)
    filter_shaped_map = models.BooleanField(null=True, default=None)
    filter_map_tier = models.ForeignKey(FilterMapTier, on_delete=models.CASCADE, null=True, default=None)
    filter_border_color = models.ForeignKey(FilterSetBorderColor, on_delete=models.CASCADE, null=True, default=None)
    filter_text_color = models.ForeignKey(FilterSetTextColor, on_delete=models.CASCADE, null=True, default=None)
    filter_background_color = models.ForeignKey(FilterSetBackgroundColor, on_delete=models.CASCADE, null=True, default=None)
    filter_font_size = models.PositiveSmallIntegerField(default=32)
    filter_sound = models.ForeignKey(FilterPlayAlertSound, on_delete=models.CASCADE, null=True, default=None)
    filter_sound_pos = models.ForeignKey(FilterPlayAlertSoundPositional, on_delete=models.CASCADE, null=True, default=None)
    filter_icon = models.ForeignKey(FilterMinimapIcon, on_delete=models.CASCADE, null=True, default=None)
    filter_beam = models.ForeignKey(FilterBeamEffect, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.filter_block
