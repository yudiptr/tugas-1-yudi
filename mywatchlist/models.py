from django.db import models

class MyWatchlistItem(models.Model):
    watched_movie = models.BooleanField()
    movie_name = models.CharField(max_length=255)
    movie_rating = models.IntegerField()
    movie_date = models.DateField()
    movie_review = models.CharField(max_length=255)