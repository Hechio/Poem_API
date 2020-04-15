from django.db import models


# Create your models here.

class Poem(models.Model):
    title = models.CharField(max_length=100)
    poem = models.CharField(max_length=1000)
    poet = models.CharField(max_length=100)
    likes = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
