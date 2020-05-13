from django.db import models


# Create your models here.
class OlxCarData(models.Model):
    brand = models.TextField(db_column='Brand', blank=True, null=True)  # Field name made lowercase.
    condition = models.TextField(db_column='Condition', blank=True, null=True)  # Field name made lowercase.
    fuel = models.TextField(db_column='Fuel', blank=True, null=True)  # Field name made lowercase.
    kms_driven = models.BigIntegerField(db_column='KMs Driven', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    price = models.BigIntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    registered_city = models.TextField(db_column='Registered City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transaction_type = models.TextField(db_column='Transaction Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'olx_car_data'
