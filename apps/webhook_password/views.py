from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import response, status
from rest_framework.views import APIView
from webhook_password.models import WebhookPassword
import json


class WebhookPasswordResetView(APIView):

    def post(self, request):
        data = request.data

        # Coleta de dados:
        user_email = data.get('user_email')

        # Cadastra evento
        WebhookPassword.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False)
        )

        # Envia e-mail
        send_mail(
            subject='Redefinição de senha',
            message='',
            from_email=f"Thércio Rodrigues <{settings.EMAIL_HOST_USER}>",
            recipient_list=[user_email],
            html_message=render_to_string('Password/password_reset_email.html', data),
            fail_silently=False,
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )


class WebhookPasswordChangedView(APIView):

    def post(self, request):
        data = request.data

        # Coleta de dados
        user_email = data.get('user_email')

        # Cadastra evento
        WebhookPassword.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False)
        )

        # Envia o e-mail
        send_mail(
            subject='Confirmação de Alteração de Senha',
            message='',
            from_email=f"Thércio Rodrigues <{settings.EMAIL_HOST_USER}>",
            recipient_list=[user_email],
            html_message=render_to_string('Password/password_changed_email.html', data),
            fail_silently=False,
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
