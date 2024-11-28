from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.webhook_notify.views import WebhookNotify

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.webhook_notify.urls', namespace='Notify')),
    path('api/v1/', include('apps.webhook_password.urls', namespace='Password')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
