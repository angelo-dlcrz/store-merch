# Generated by Django 5.0.2 on 2024-03-16 16:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='biography',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(default='RK', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='official_homepage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2024)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='band',
            name='name',
            field=models.CharField(choices=[('AR', 'Alternative Rock'), ('RK', 'Rock'), ('PR', 'Pop Rock'), ('SR', 'Soft Rock')], max_length=5),
        ),
    ]
