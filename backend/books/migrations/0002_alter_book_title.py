# Generated by Django 4.1 on 2023-03-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=80, unique=True, verbose_name='Book Title'),
        ),
    ]
