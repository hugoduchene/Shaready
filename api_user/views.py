from user.models import Subscription, CustomUser
from rest_framework.views import APIView
from utils.notification import ManageNotification
from rest_framework.response import Response
from api_user.serializer import (
    SubscriptionSerializer, 
    AllInfosUserSerializer,
    ResearchUserSerializer,
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CreateSubscribe(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pseudoUser):
        serializer = SubscriptionSerializer(data=request.data)
        
        subscribe = Subscription.objects.filter(
            id_giving = request.user,
            id_receiving = request.data.get("id_receiving", "")
        )
        subscribe_is_exist = subscribe.count()
        
        if serializer.is_valid(raise_exception=True):
            if subscribe_is_exist == 0:
                ManageNotification().create_notification(request.user, pseudoUser, 1)
                serializer.save(id_giving=request.user)
            else:
                serializer.save(id_giving=request.user)
                subscribe.delete()
            Subscription.already_follow = subscribe.count()
            Subscription.nbs_follows = Subscription.objects.filter(
                id_receiving= request.data.get("id_receiving", "")
            ).count()
            return Response(serializer.data)

class GetAllInfoUser(APIView):

    def get(self, request, idUser):
        user = CustomUser.objects.filter(id=idUser)
        
        CustomUser.info_user = {
            "nbs_gold_likes" : user[0].likearticle_set.filter(
                reaction=1
            ).count(),

            "nbs_folows" : Subscription.objects.filter(
                id_receiving=user[0]
            ).count()
        }
        serializer = AllInfosUserSerializer(user, many=True)
        return Response(serializer.data)
        

class ResearchUser(APIView):

    def get(self, request, userSearch):
        user = CustomUser.objects.filter(username__icontains=userSearch)
        serializer = ResearchUserSerializer(user, many=True)
        return Response(serializer.data)
        
class AlreadySubscribed(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, idReceiving):
        already_sub = {
            "already_sub" : Subscription.objects.filter(
                id_giving = request.user,
                id_receiving = idReceiving,
                ).count()
        }

        return Response(already_sub)
        
        



        



    