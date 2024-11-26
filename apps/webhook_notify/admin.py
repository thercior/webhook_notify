from django.contrib import admin
from webhook_notify.models import WebhookNotify
from import_export.admin import ImportExportMixin


@admin.register(WebhookNotify)
class WebhookNotifyAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'event_type', 'event')
    list_filter = ('event_type',)
