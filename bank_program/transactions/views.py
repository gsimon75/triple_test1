from rest_framework import mixins, serializers, viewsets

from transactions import models


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ["id", "program", "bank", "country"]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionSerializer(serializers.Serializer):
    is_eligible = serializers.BooleanField(default=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class TransactionViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        pass

