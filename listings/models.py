from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):
        ALTERNATIVE_ROCK = 'AR'
        ROCK = 'RK'
        POP_ROCK = 'PR'
        SOFT_ROCK = 'SR'

    name = models.fields.CharField(max_length=50)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(2024),
        ]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLO'
        POSTERS = 'POS'
        MISCELLANEOUS = 'MSC'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2024),
        ],
        null=True,
        blank=True,
    )
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(
        Band,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'{self.title}'
