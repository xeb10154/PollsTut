import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # 1 >= 1 - 1


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Movie(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=16)
    movies = models.ManyToManyField(
        'Movie', through='Casting', related_name='characters')

    def __str__(self):
        return self.name


class Casting(models.Model):
    movie = models.ForeignKey(
        Movie, related_name='castings', on_delete=models.SET_NULL, null=True)
    character = models.ForeignKey(
        Character, related_name='castings', on_delete=models.SET_NULL, null=True)
    pay = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.name
