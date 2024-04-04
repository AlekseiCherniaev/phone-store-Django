from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from phone_store_for_GITHUB import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('user/', include('user.urls', namespace='user')),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'product.views.handler404'

admin.site.site_header = 'Панель администрировния'
admin.site.index_title = 'Телефоны для продажи'
