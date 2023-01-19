from django.db import models


class Country(models.Model):
    Country_Name=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.Country_Name

class Cap(models.Model):
    Country_Name=models.ForeignKey(Country,on_delete=models.CASCADE)
    Cap_name=models.CharField(max_length=100)
    num_states=models.IntegerField()

        
