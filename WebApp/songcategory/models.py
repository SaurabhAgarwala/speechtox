from django.db import models

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=50)
    song_name = models.CharField(max_length=50)

    def __str__(self):
        return self.song_name