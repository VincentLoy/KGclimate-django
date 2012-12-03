from django.db import models

class Climate_Class(models.Model):
    climate_class = models.CharField(max_length=10)
    def __unicode__(self):
        return self.climate_class

class Scenario(models.Model):
    scenario = models.CharField(max_length=10)
    def __unicode__(self):
        return self.scenario

class Year_Range(models.Model):
    year_range = models.CharField(max_length=10)
    def __unicode__(self):
        return self.year_range

class Coordinate(models.Model):
    climate_class = models.ForeignKey(Climate_Class)
    scenario = models.ForeignKey(Scenario)
    year_range = models.ForeignKey(Year_Range)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)

