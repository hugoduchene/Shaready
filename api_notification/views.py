from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from user.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from user.models import Notification
from django.core.paginator import Paginator
from api_notification.serializer import (
    NbsNotificationSerializer,
    AllDataNotificationSerializer,
)

# Create your views here.

class NbsNotification(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        all_notif = {
            "all_notification" : Notification.objects.filter(
                id_receiving=request.user, 
                read=False
            ).count()
        }
        
        return Response(all_notif)

class ManageNotification(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        test = Notification.objects.filter(
            id_receiving=request.user, 
            read=False
        ).update(read=True)

        return Response("OK")

class GetAllNotification(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, idPage):
        all_notifications = Notification.objects.filter(id_receiving=request.user).order_by('-date_notification')
        objects_page = Paginator(all_notifications, 15).get_page(idPage).object_list
        for object_notification in objects_page:
            object_notification.infos_user = {
                "image_profile" : str(object_notification.id_giving.image_profile),
                "pseudo" : object_notification.id_giving.username
            }
            
        serializer = AllDataNotificationSerializer(objects_page, many=True)
        return Response(serializer.data)
        




