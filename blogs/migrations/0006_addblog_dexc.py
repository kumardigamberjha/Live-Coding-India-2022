# Generated by Django 4.0.1 on 2022-02-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_addblog_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblog',
            name='dexc',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]