# Generated by Django 3.0.7 on 2020-06-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='brewery',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
