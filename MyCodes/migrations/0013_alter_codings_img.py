# Generated by Django 4.0.1 on 2022-02-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCodes', '0012_codings_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codings',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]