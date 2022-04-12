import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField

from banks.models import Bank
from programs.models import Program

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.TextField(null=True)
    bank = models.TextField(null=True)
    country = models.TextField(null=True)
    error = models.TextField(null=True)
    is_eligible = models.BooleanField(default=False)
