# Generated by Django 4.0.1 on 2022-02-16 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyCodes', '0006_category_hackerrankproblemsolving_proj_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hackerrankproblemsolving',
            old_name='category',
            new_name='cat',
        ),
        migrations.RenameField(
            model_name='pythonforbegginers',
            old_name='category',
            new_name='cat',
        ),
        migrations.RenameField(
            model_name='webdesign',
            old_name='category',
            new_name='cat',
        ),
    ]
