from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Sponsorship(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    farmer_name = models.CharField(max_length=100)
    amount = models.FloatField()
    crop = models.CharField(max_length=50)
    quantity = models.FloatField()
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.farmer_name} - {self.crop} ({self.amount} TND)"

# Create your models here.
