from django.db import models
from django.urls import reverse


# Create your models here.
class PhoneCategory(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class PhoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity__gt=0)


class PhoneProduct(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(PhoneCategory, on_delete=models.PROTECT, related_name='products')
    image = models.ImageField(upload_to='product/static/product/img', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)

    objects = models.Manager()
    phone_objects = PhoneManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
