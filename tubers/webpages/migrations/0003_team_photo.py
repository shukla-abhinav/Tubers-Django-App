# Generated by Django 3.1.7 on 2021-03-28 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/slider/%Y/'),
            preserve_default=False,
        ),
    ]
