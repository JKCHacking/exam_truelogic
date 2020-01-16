from django.db import models

# Create your models here.
class Current_User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

class lead(models.Model):
    bussiness_name = models.CharField(max_length=100)
    bussiness_address = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)

class safebrowsing(models.Model):
    status = models.CharField(max_length=100)
