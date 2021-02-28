from django.db import models


class Notify(models.Model):
    receiver = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    service_request = models.CharField(max_length=200)
    type = models.CharField(max_length=20, validators=[], default="PENDING")

