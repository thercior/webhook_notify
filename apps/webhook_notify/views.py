from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import response, status
from rest_framework.views import APIView
from webhook_notify.messages import test_message, purchase_course_message
from webhook_notify.models import WebhookNotify
from services.callmebot import CallMeBot
from utils.format import format_currency
import json


class PurchaseCourseView(APIView):

    def post(self, request):
        data = request.data

        user_email = settings.USER_EMAIL
        product = data.get('Product')['product_name']
        created_at = data.get('created_at')
        client = data.get('Customer')['full_name']
        cpf = data.get('Customer')['CPF']
        cell_phone = data.get('Customer')['mobile']
        email_client = data.get('Customer')['email']
        product_type = 'membros' if data.get('product_type') == 'membership' else 'avulsos'
        product_id = data.get('Product')['product_id']
        order = data.get('order_id')
        status_purchase = 'pago' if data.get('order_status') == 'paid' else 'pendente/cancelado'
        payment_method = data.get('payment_method')
        product_value = data.get('Commissions')['charge_amount']
        product_commission = data.get('Commissions')['my_commission']
        next_payment = data.get('Subscription')['next_payment']

        # Cadastrar evento
        WebhookNotify.objects.create(
            event_type=data.get('webhook_event_type'),
            event=json.dumps(data, ensure_ascii=False)
        )

        message = purchase_course_message.format(
            product,
            created_at,
            client,
            cpf,
            cell_phone,
            email_client,
            product_type,
            product_id,
            product,
            order,
            status_purchase,
            payment_method,
            format_currency(product_value),
            format_currency(product_commission),
            next_payment
        )

        callmebot = CallMeBot()
        callmebot.send_message(message)

        data['Commissions']['charge_amount'] = format_currency(data.get('Commissions')['charge_amount'])
        data['Commissions']['my_commission'] = format_currency(data.get('Commissions')['my_commission'])

        send_mail(
            subject=f'Kiwify App - Aviso de compra do {product}',
            message='',
            from_email=f'<{settings.EMAIL_HOST_USER}',
            recipient_list=[user_email],
            html_message=render_to_string('purchase_course.html', data),
            fail_silently=False
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )


class TestNotifyView(APIView):

    def post(self, request):
        data = request.data
        print(data)

        event = data.get('event')
        date_message = data.get('date_message')
        name = data.get('name')
        client_email = data.get('client_email')
        client_phone = data.get('client_phone')
        sector = data.get('sector')

        WebhookNotify.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False)
        )

        message = test_message.format(
            event,
            date_message,
            name,
            client_email,
            client_phone,
            sector
        )

        callmebot = CallMeBot()
        callmebot.send_message(message)

        send_mail(
            subject=f'Email de {event}',
            message='',
            from_email=f'<{settings.EMAIL_HOST_USER}',
            recipient_list=[client_email],
            html_message=render_to_string('test_event.html', data),
            fail_silently=False
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )
