from django.db import models

# Create your models here.
class Artist(models.Model):
    aka = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'artist'
