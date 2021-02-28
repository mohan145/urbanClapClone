from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    locality = models.CharField(max_length=20, default=None, null=True)
    availability = models.BooleanField(default=False)
    service_type = models.CharField(max_length=20, default=None, null=True)
    user_type = models.CharField(max_length=20, validators=[])
