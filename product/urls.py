from django.urls import path, register_converter
from product import views, converters

register_converter(converters.FourDigitConverter, 'year4')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('product/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
    path('category/<slug:category_slug>/', views.ProductForCategory.as_view(), name='category'),
    path('products_for_year/<year4:year>/', views.products_for_year, name='products_for_year'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),

]
