from django.db import models

# Create your models here.
class NumberOfSongs(models.Model):
    number_of_songs = models.IntegerField()

    def __str__(self):
        return self.number_of_songs