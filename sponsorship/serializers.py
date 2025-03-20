from rest_framework import serializers
from .models import Sponsor, Sponsorship

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'phone']

class SponsorshipSerializer(serializers.ModelSerializer):
    sponsor_name = serializers.CharField(write_only=True)
    sponsor_phone = serializers.CharField(write_only=True)
    sponsor = SponsorSerializer(read_only=True)

    class Meta:
        model = Sponsorship
        fields = ['id', 'sponsor', 'sponsor_name', 'sponsor_phone', 'farmer_name', 'amount', 'crop', 'quantity', 'start_date', 'status']
        read_only_fields = ['sponsor', 'start_date', 'status']

    def create(self, validated_data):
        # Extract sponsor data
        sponsor_data = {
            'name': validated_data.pop('sponsor_name'),
            'phone': validated_data.pop('sponsor_phone')
        }
        # Create sponsor
        sponsor = Sponsor.objects.create(**sponsor_data)
        # Prepare sponsorship data, excluding sponsor_name/phone
        sponsorship_data = {
            'sponsor': sponsor,
            'farmer_name': validated_data['farmer_name'],
            'amount': validated_data['amount'],
            'crop': validated_data['crop'],
            'quantity': validated_data['quantity']
        }
        # Create sponsorship
        return Sponsorship.objects.create(**sponsorship_data)