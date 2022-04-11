from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status, mixins, serializers, viewsets

from transactions import models
from banks.models import Bank
from programs.models import Program

import logging

logger = logging.getLogger(__name__)


class TransactionSerializer(serializers.Serializer):
    is_eligible = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return models.Transaction.objects.create(
            program=validated_data["program"],
            bank=validated_data["bank"],
            country=validated_data["country"]
        )

    def update(self, instance, validated_data):
        pass


class TransactionViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        country = self.request.data.get('country')
        currency = self.request.data.get('currency')
        program_name = self.request.data.get('program')
        bank_name = self.request.data.get('bank')

        program = Program.objects.filter(name=program_name)
        bank = Bank.objects.filter(name=bank_name)
        error = None

        if not program:
            error = f"Invalid program {program_name}"
        elif currency != program[0].currency:
            error = f"Currency {currency} does not match program {program_name}"
        elif not bank:
            error = f"Invalid bank {bank_name}"
        elif country not in bank[0].countries:
            error = f"Country {country} not supported by bank {bank_name}"

        if error is not None:
            logger.error(error)
            raise ValidationError(error, code=400)

        serializer.save(country=country, program=program[0].id, bank=bank[0].id)

