# Generated by Django 4.0.1 on 2022-12-25 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_usermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]