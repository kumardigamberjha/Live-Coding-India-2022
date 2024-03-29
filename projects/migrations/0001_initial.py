# Generated by Django 4.0.1 on 2022-12-25 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('last_modified', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now=True)),
                ('content', models.TextField(blank=True)),
                ('content1', models.TextField(blank=True)),
                ('content2', models.TextField(blank=True)),
                ('author', models.CharField(default='Coding India', max_length=30)),
                ('category', models.CharField(max_length=150)),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.playlist')),
            ],
        ),
    ]
