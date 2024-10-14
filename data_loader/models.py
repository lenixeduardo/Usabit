from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=255)
    imdb_rating = models.CharField(max_length=10)
    plot = models.TextField()

    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name