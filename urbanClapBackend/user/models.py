from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    locality = models.CharField(max_length=20, default=None)
    availability = models.BooleanField()
    service_type = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, validators=[])
