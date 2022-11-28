from enum import Enum

from django.core import validators
from django.db import models

class Profile(models.Model):
    MIN_AGE = 12
    MAX_PASSWORD = 30
    MAX_FIRST_NAME = 30
    MAX_LAST_NAME = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(MIN_AGE)
        ]
    )
    password = models.CharField(
        max_length=MAX_PASSWORD,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=MAX_FIRST_NAME,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=MAX_LAST_NAME,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.email

    def full_name(self):
        return f'{self.first_name}-{self.last_name}'


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class GameChoices(ChoicesEnum):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'


class Game(models.Model):
    MAX_TITLE_LEN = 30
    MAX_CATEGORY_LEN = 15

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
        unique=True,
        blank=False,
        null=False,
    )
    category = models.CharField(
        max_length=MAX_CATEGORY_LEN,
        choices=GameChoices.choices(),
        null=False,
        blank=False,
    )
    rating = models.FloatField(
        validators=[
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5.0),
        ],
        blank=False,
        null=False,
    )
    max_level = models.PositiveIntegerField(
        verbose_name='Max Level',
        validators=[
            validators.MinValueValidator(1)
        ],
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        verbose_name='Image URL',
        blank=False,
        null=False,
    )
    summary = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title