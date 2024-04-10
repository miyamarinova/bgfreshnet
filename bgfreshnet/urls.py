from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bgfreshnet.common.urls')),
    path('accounts/', include('bgfreshnet.accounts.urls')),
    path('products/', include('bgfreshnet.freshnet_products.urls')),
    path('news/', include('bgfreshnet.news.urls')),
    path('events/', include('bgfreshnet.events.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
