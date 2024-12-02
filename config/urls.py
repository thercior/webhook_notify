from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.webhook_notify.views import WebhookNotify
from config.views import APIRootView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.webhook_notify.urls', namespace='Notify')),
    path('api/v1/', include('apps.webhook_password.urls', namespace='Password')),
    path('api/v1/', APIRootView.as_view(), name='api-root'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
