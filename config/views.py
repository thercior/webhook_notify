from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({
            'Alteração de Senha': reverse('Password:changed_password', request=request),
            'Notificação de compra de curso': reverse('Notify:notify_purchase_course', request=request),
            'Reset de Senha': reverse('Password:reset_password', request=request),
        })
