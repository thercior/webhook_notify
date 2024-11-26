from django.urls import path
from webhook_password.views import WebhookPasswordChangedView, WebhookPasswordResetView


app_name = 'Password'

urlpatterns = [
    path('password/changed/', WebhookPasswordChangedView.as_view(), name='changed_password'),
    path('password/reset/', WebhookPasswordResetView.as_view(), name='reset_password'),
]
