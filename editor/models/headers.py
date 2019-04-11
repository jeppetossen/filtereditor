from django.db import models


class HeaderSection(models.Model):
    header_section = models.CharField(max_length=100, null=True, default=None)

    def __unicode__(self):
        return self.header_section


class HeaderSubSection(models.Model):
    header_subsection = models.CharField(max_length=100, null=True, default=None)
    header_section = models.ForeignKey(HeaderSection, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.header_subsection


class HeaderBlockSection(models.Model):
    header_block_section = models.CharField(max_length=100, null=True, default=None)
    header_subsection = models.ForeignKey(HeaderSubSection, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.header_block_section


class HeaderBlock(models.Model):
    header_block = models.CharField(max_length=100, null=True, default=None)
    header_subsection = models.ForeignKey(HeaderSubSection, on_delete=models.CASCADE, null=True, default=None)
    header_block_subsection = section = models.ForeignKey(HeaderBlockSection, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.header_block
