# Generated by Django 4.0.3 on 2022-03-08 08:10

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('program', models.TextField(unique=True)),
                ('bank', models.TextField(unique=True)),
                ('country', models.TextField(unique=True)),
            ],
        ),
    ]

 # TODO fk constraints:
 # - only valid program
 # - only valid bank
 # - only such a country that is valid for bank
