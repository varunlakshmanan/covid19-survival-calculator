from django.db import models
import os
import pandas as pd


class Person(models.Model):
    region = models.TextField()
    country = models.TextField()
    age = models.IntegerField()
    death = models.BooleanField()
    male = models.BooleanField()
    female = models.BooleanField()
    symptom_onset_hospitalization = models.IntegerField()
    mortality_rate = models.FloatField()
    pop_density = models.FloatField()
    high_risk_travel = models.BooleanField()

    def __str__(self):
        return str(self.region) + ', ' + str(self.country)

    @staticmethod
    def to_data_frame():
        people = Person.objects.all()
        data = {
            'region': [],
            'country': [],
            'age': [],
            'death': [],
            'male': [],
            'female': [],
            'symptom_onset_hospitalization': [],
            'mortality_rate': [],
            'pop_density': [],
            'high_risk_travel': []
        }
        for person in people:
            data['region'].append(person.location)
            data['country'].append(person.country)
            data['age'].append(person.age)
            data['death'].append(int(person.death))
            data['male'].append(int(person.male))
            data['female'].append(int(person.female))
            data['symptom_onset_hospitalization'].append(person.symptom_onset_hospitalization)
            data['mortality_rate'].append(person.mortality_rate)
            data['pop_density'].append(person.pop_density)
            data['high_risk_travel'].append(int(person.high_risk_travel))
        return pd.DataFrame(data)

    @staticmethod
    def to_new_csv():
        df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data', 'datasets', 'data.csv'))
        df2 = Person.to_data_frame()
        df.append(df2).sort_values(['country', 'region']).reset_index(drop=True).to_csv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'datasets', 'new_data.csv'), index=False)
