# Generated by Django 3.1.1 on 2021-04-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiels', '0002_travauxdemande_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='materiel',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='travauxdemande',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]