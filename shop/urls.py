from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('', include('core.urls')), # includes core url
    path('items/', include('item.urls')), # includes item url
    path('dashboard', include('dashboard.urls')), # includes dashboard url
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
