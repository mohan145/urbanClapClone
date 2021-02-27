from django.db import models

class User(models.Model):
    service_type = models.CharField(max_length=100)
    description = models.CharField(max_length=20)
    client_id = models.CharField(max_length=500)
    provider_id = models.CharField(max_length=20, default=None, null=True)
    status = models.BooleanField()
    service_type = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, validators=[])

