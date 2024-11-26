from django.urls import path
from apps.webhook_notify.views import PurchaseCourseView, TestNotifyView


app_name = 'Notify'

urlpatterns = [
    path('notify/purchase_course/', PurchaseCourseView.as_view(), name='notify_purchase_course'),
    path('notify/teste_notify/', TestNotifyView.as_view(), name='notify_test'),
]
