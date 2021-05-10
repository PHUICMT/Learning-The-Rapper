from django.db import models
from artist.models import Artist

# Create your models here.
class Single(models.Model):
    Single = models.ForeignKey(Artist, to_field='id', on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=100)
    youtube_view = models.IntegerField()

    class Meta:
        db_table = 'single'

