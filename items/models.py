from django.db import models
# from django_countries.fields import CountryField
# from django_countries.countries import COUNTRIES

# Create your models here.

class GroceryItems(models.Model):
    name = models.CharField(max_length=50)
    wholesale_price = models.CharField(max_length=10)
    retail_price = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    entry_date = models.DateField()

    class Meta:
        db_table = 'grocery'

    def __str__(self) -> str:
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)
    owner = models.CharField(max_length=40)
    mob = models.CharField(max_length=10)

    class Meta:
        db_table = 'store'

    def __str__(self) -> str:
        return self.name



