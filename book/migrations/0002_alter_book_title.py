# Generated by Django 4.1.7 on 2023-03-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]