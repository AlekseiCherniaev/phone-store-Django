from django.urls import path, register_converter
from product import views, converters

register_converter(converters.FourDigitConverter, 'year4')

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product/<slug:product_slug>', views.product, name='product'),
    path('products_for_year/<year4:year>/', views.products_for_year, name='products_for_year'),

]
