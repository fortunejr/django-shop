from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('core.urls')),
    path('inbox/', include('conversation.urls')),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
