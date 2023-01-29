from django.db import models


# Create your models here.
class Item(models.Model):
    art_number = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    original_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ean_code = models.CharField(max_length=50)
    image_name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    class Meta:
        db_table = "items"
