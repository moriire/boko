# Generated by Django 4.0.6 on 2023-03-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('md', 'MD'), ('librarian', 'librarian')], max_length=20),
        ),
    ]
