from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

class Artist(models.Model):
    id = models.IntegerField()
    gid = models.CharField()
    name = models.CharField()
    sort_name = models.CharField()
    area = models.CharField()
    aliases = ListField(EmbeddedModelField('Aliase'))
    begin = EmbeddedModelField('Begin')
    end = EmbeddedModelField('End')
    tags = ListField(EmbeddedModelField('Tag'))
    rating = EmbeddedModelField('Rating')

class Aliase(model.Model):
    name = models.CharField()
    sort_name = models.CharField()

class Begin(model.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()

class End(model.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()

class Tag(model.Model):
    count = models.IntegerField()
    value = models.CharField()

class Rating(model.Model):
    count = models.IntegerField()
    value = models.CharField()
