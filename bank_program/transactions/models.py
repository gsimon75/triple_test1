import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.TextField(unique=True)
    bank = models.TextField(unique=True)
    country = models.TextField(unique=True)
