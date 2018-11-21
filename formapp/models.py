from django.db import models
class Address(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    mobile_number = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    salary = models.IntegerField()
    comm = models.IntegerField()
    location = models.CharField(max_length=30)

