from django.contrib import admin
from webhook_password.models import WebhookPassword
from import_export.admin import ImportExportMixin


@admin.register(WebhookPassword)
class WebhookNotifyAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'event_type', 'event')
    list_filter = ('event_type',)
