from django.db import models
from djangotoolbox.fields import ListField

class Artist(models.Model):
    id = models.IntegerField()
    gid = models.CharField()
    name = models.CharField()
    sort_name = models.CharField()
    area = models.CharField()
    aliases = ListField()

    tags = ListField()
    comments = ListField()

class Dict(models.Model):
    name = models.CharField()

class KeyVal(models.Model):
    container = models.ForeignKey(Dict)
    key       = models.CharField()
    value     = models.CharField()
