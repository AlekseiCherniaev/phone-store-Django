from django.urls import path
from product import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.AllProductsPageView.as_view(), name='products'),
    path('product/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
    path('category/<slug:category_slug>/', views.ProductForCategory.as_view(), name='category'),
    path('add-product/', views.AddProduct.as_view(), name='add_product'),
]
