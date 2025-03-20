from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Produce(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.CharField(max_length=50)
    quantity = models.FloatField()  # kg
    price_per_kg = models.FloatField()  # TND/kg

    def __str__(self):
        return f"{self.crop} ({self.quantity} kg)"

class Transaction(models.Model):
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_phone = models.CharField(max_length=20)
    total_price = models.FloatField()  # Includes 2% fee

    def __str__(self):
        return f"{self.buyer_name} - {self.produce}"

# Create your models here.
