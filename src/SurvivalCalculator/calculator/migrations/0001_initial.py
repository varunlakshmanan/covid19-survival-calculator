# Generated by Django 3.0.4 on 2020-03-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('country', models.TextField()),
                ('age', models.IntegerField()),
                ('death', models.BooleanField()),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('symptom_onset_hospitalization', models.IntegerField()),
                ('mortality_rate', models.FloatField()),
                ('population_density', models.FloatField()),
                ('high_risk_travel', models.BooleanField()),
            ],
        ),
    ]
