# Generated by Django 3.1.1 on 2021-07-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiels', '0004_categories_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiel',
            name='reference',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
