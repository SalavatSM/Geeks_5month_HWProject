from django.db import models
from django.db.models import Avg


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        return self.director.name if self.director else 'No director.'

    @property
    def rating(self):
        return self.reviews.aggregate(avg_rating=Avg('stars'))['avg_rating']


STAR_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* '),
)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movie_reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

    def __str__(self):
        return self.text

    # @property
    # def average_rating(self):
    #     average_rat = sum(self.stars) / len(self.stars)
    #     # print(average_rat)
    #     return average_rat

