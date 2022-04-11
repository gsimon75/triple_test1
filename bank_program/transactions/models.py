import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField

from banks.models import Bank
from programs.models import Program

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # program = models.ForeignKey(Program, on_delete=models.CASCADE)
    program = models.UUIDField()
    # bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bank = models.UUIDField()
    country = models.TextField(unique=True)
    is_eligible = models.BooleanField(default=True)
