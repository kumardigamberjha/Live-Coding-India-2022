# Generated by Django 4.0.1 on 2022-01-27 16:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCodes', '0004_hackerrankproblemsolving_pythonforbegginers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now=True)),
                ('category', models.CharField(blank=True, max_length=200)),
                ('HTML', ckeditor.fields.RichTextField(blank=True)),
                ('Css', ckeditor.fields.RichTextField(blank=True)),
                ('Js', ckeditor.fields.RichTextField(blank=True)),
                ('author', models.CharField(default='Coding India', max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='hackerrankproblemsolving',
            name='author',
            field=models.CharField(default='Coding India', max_length=150),
        ),
        migrations.AlterField(
            model_name='pythonforbegginers',
            name='author',
            field=models.CharField(default='Coding India', max_length=150),
        ),
    ]
