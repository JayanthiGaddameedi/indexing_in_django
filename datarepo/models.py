from django.db import models
from django.db.models import Index


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            Index(fields=['name'])
        ]
