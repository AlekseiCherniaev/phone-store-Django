from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler404 = 'product.views.handler404'

admin.site.site_header = 'Панель администрировния'
admin.site.index_title = 'Телефоны для продажи'