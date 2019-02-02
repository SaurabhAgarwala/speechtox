from django.db import models

# Create your models here.
class Content(models.Model):
    ipfn = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ipfn