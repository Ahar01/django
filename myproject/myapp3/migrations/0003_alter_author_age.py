# Generated by Django 4.2.15 on 2024-08-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0002_author_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default='20'),
        ),
    ]
