# Generated by Django 4.0.1 on 2022-01-27 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyCodes', '0002_rename_python_for_beginners_playlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='play',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyCodes.playlist'),
            preserve_default=False,
        ),
    ]
