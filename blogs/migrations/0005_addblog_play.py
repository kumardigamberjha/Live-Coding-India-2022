# Generated by Django 4.0.1 on 2022-01-28 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblog',
            name='play',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.playlist'),
            preserve_default=False,
        ),
    ]