# Generated by Django 3.2.6 on 2021-08-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0007_auto_20210804_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]