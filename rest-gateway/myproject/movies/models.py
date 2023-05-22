from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title