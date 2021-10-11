from django.db import models

# Create your models here.
from django.db.models import IntegerField, TextField


class RequestLog(models.Model):
    visits = IntegerField(default=0)
    user_agent = TextField(null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
