# Generated by Django 4.0.1 on 2022-03-14 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]