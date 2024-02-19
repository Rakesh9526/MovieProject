# Generated by Django 5.0 on 2024-02-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_alter_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
