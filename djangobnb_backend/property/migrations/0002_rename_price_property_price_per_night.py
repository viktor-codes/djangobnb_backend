# Generated by Django 5.0.6 on 2024-06-14 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='price',
            new_name='price_per_night',
        ),
    ]
