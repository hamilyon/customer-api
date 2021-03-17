from django.db import models
from concurrency.fields import IntegerVersionField
import datetime




class Company(models.Model):
    pass


class Customer(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    status = models.CharField(max_length=11) #"prospective", "current" or "non-active"
    creationDate = models.DateField(default=datetime.date.today)    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="customers")
    version = IntegerVersionField()


class CustomerNote(models.Model):
    text = models.CharField(max_length=60)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="notes")
    version = IntegerVersionField()
