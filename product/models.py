from django.db import models


# Create your models here.
class PhoneCategory(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name


class PhoneProduct(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(PhoneCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/static/product/img', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
