# Generated by Django 5.0 on 2023-12-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='exit', upload_to=''),
            preserve_default=False,
        ),
    ]
