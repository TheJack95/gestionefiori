from django.db import models


# Create your models here.
class Item(models.Model):
    artNumber = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    originalPrice = models.DecimalField
    price = models.DecimalField
    eanCode = models.CharField(max_length=50)
    imageName = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)

    class Meta:
        db_table = "items"
