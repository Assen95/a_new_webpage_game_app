# Generated by Django 4.1.3 on 2022-11-27 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('PUZZLE', 'Puzzle'), ('STRATEGY', 'Strategy'), ('SPORTS', 'Sports'), ('BOARD_CARD_GAME', 'Board/Card Game'), ('OTHER', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(5.0)])),
                ('max_level', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField()),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(12)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]