# Generated by Django 4.0.8 on 2022-11-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshelf',
            name='isbn_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='bookshelf',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
