# Generated by Django 3.1.2 on 2020-10-20 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_auto_20201020_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='sq_fit',
            new_name='bathrooms',
        ),
    ]
