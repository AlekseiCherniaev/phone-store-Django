from django.db import models
from django.urls import reverse


# Create your models here.
class PhoneCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class PhoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity__gt=0)


class PhoneProduct(models.Model):
    name = models.CharField(max_length=120, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(PhoneCategory, on_delete=models.PROTECT, related_name='products',
                                 verbose_name='Категория')
    image = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Изображение')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='Слаг')
    tag = models.ManyToManyField('PhoneTag', blank=True, related_name='tags', verbose_name='Тэг')

    objects = models.Manager()
    phone_objects = PhoneManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Телефоны'
        verbose_name_plural = 'Телефоны'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


class PhoneTag(models.Model):
    tag = models.CharField(max_length=120, verbose_name='Название')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['tag']
