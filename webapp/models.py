from djongo import models

class Artist(models.Model):
    #id = models.IntegerField()
    gid = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    sort_name = models.CharField(max_length=30)
    area = models.CharField(max_length=20)
    aliases = models.ListField(models.EmbeddedModelField('Aliase'))
    begin = models.EmbeddedModelField('Begin')
    end = models.EmbeddedModelField('End')
    tags = models.ListField(models.EmbeddedModelField('Tag'))
    rating = models.EmbeddedModelField('Rating')

    objects = models.DjongoManager()

class Aliase(models.Model):
    name = models.CharField(max_length=30)
    sort_name = models.CharField(max_length=30)

class Begin(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()

class End(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()

class Tag(models.Model):
    count = models.IntegerField()
    value = models.CharField(max_length=30)

class Rating(models.Model):
    count = models.IntegerField()
    value = models.CharField(max_length=100)
