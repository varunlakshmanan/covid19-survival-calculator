# Generated by Django 3.0.4 on 2020-03-28 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='population_density',
            new_name='pop_density',
        ),
    ]
