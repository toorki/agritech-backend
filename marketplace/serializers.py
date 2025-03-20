from rest_framework import serializers
from .models import Farmer, Produce, Transaction

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id', 'name', 'phone']

class ProduceSerializer(serializers.ModelSerializer):
    farmer_name = serializers.CharField(write_only=True)
    farmer_phone = serializers.CharField(write_only=True)
    farmer = FarmerSerializer(read_only=True)

    class Meta:
        model = Produce
        fields = ['id', 'farmer', 'farmer_name', 'farmer_phone', 'crop', 'quantity', 'price_per_kg']
        read_only_fields = ['farmer']

    def create(self, validated_data):
        farmer_data = {
            'name': validated_data.pop('farmer_name'),
            'phone': validated_data.pop('farmer_phone')
        }
        farmer = Farmer.objects.create(**farmer_data)
        validated_data['farmer'] = farmer
        return Produce.objects.create(**validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    produce = ProduceSerializer(read_only=True)
    produce_id = serializers.PrimaryKeyRelatedField(
        queryset=Produce.objects.all(), source='produce', write_only=True
    )

    class Meta:
        model = Transaction
        fields = ['id', 'produce', 'produce_id', 'buyer_name', 'buyer_phone', 'total_price']
        read_only_fields = ['produce', 'total_price']

    def create(self, validated_data):
        # Calculate total_price before creating the transaction
        produce = validated_data['produce']
        total_price = produce.quantity * produce.price_per_kg * 1.02  # 2% fee
        validated_data['total_price'] = total_price
        # Create transaction with all required fields
        return Transaction.objects.create(**validated_data)