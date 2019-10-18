from django.db import models


class HeaderSection(models.Model):
    section = models.CharField(max_length=100, null=True, default=None)

    def __unicode__(self):
        return self.header_section


class HeaderSubSection(models.Model):
    subsection = models.CharField(max_length=100, null=True, default=None)
    parent = models.ForeignKey(HeaderSection, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.subsection


class HeaderBlockSection(models.Model):
    blocksection = models.CharField(max_length=100, null=True, default=None)
    domain = models.ForeignKey(HeaderSection, on_delete=models.CASCADE, null=True, default=None)
    #parent = models.ForeignKey(HeaderSubSection, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.blocksection


class HeaderBlock(models.Model):
    block = models.CharField(max_length=100, null=True, default=None)
    #domain = models.CharField(max_length=100, null=True, default=None)
    domain = models.ForeignKey(HeaderSection, on_delete=models.CASCADE, null=True, default=None)

    
    #parent = models.ForeignKey(HeaderSubSection, on_delete=models.CASCADE, null=True, default=None)
    #parent = models.ForeignKey(HeaderBlockSection, on_delete=models.CASCADE, null=True, default=None)

    def __unicode__(self):
        return self.block
