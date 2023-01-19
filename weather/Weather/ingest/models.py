from django.db import models
class weather_records(models.Model):
    dates=models.DateField(primary_key=True)
    Max_temp=models.IntegerField()
    Min_temp=models.IntegerField()
    Precipitation=models.IntegerField()

class yield_records(models.Model):
    yield_year=models.IntegerField(primary_key=True)
    yield_data=models.IntegerField()

class result(models.Model):
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    Max_temp=models.IntegerField(null=True)

class result1(models.Model):
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    Min_temp=models.IntegerField(null=True)
class result2(models.Model):
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    Precipitation=models.IntegerField(null=True)
    


