from django.db import models


class Services(models.Model):
    service_type = models.CharField(max_length=30)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    client_id = models.CharField(max_length=20)
    provider_id = models.CharField(max_length=20, default=None, null=True)
    status = models.CharField(max_length=20, validators=[], default="PENDING")

