from rest_framework import mixins, serializers, viewsets

from transactions import models
from banks.models import Bank
from programs.models import Program

import logging

logger = logging.getLogger(__name__)


class TransactionSerializer(serializers.Serializer):
    is_eligible = serializers.BooleanField(default=True)

    def create(self, validated_data):
        program = Program.objects.filter(name=validated_data["program"])
        bank = Bank.objects.filter(name=validated_data["bank"])

        if not program:
            logger.error("Invalid program {validated_data['program']}")
            return

        if validated_data["currency"] != program[0].currency:
            logger.warning(f"Currency {validated_data['currency']} does not match program {program[0].name}")
            return

        if not bank:
            logger.error("Invalid bank {validated_data['bank']}")
            return

        if validated_data["country"] not in bank[0].countries:
            logger.warning(f"Country {validated_data['country']} not supported by bank {bank[0].name}")
            return

        return models.Transaction.objects.create(
            program=program[0].id,
            bank=bank[0].id,
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
        program = self.request.data.get('program')
        bank = self.request.data.get('bank')
        serializer.save(country=country, currency=currency, program=program, bank=bank)

