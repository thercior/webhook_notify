from django.db import models
import uuid


class WebhookPassword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=50, null=True, blank=True)
    event = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Webhook Password'
        verbose_name_plural = 'Webhooks Passwords'

    def __str__(self):
        return f'{str(self.id)} - {str(self.event_type)}'
