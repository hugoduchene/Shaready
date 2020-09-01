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
from rest_framework.renderers import JSONRenderer


""" Shows the number of registered members """


class NbsUser(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        nbs_user = {"nbs_user": CustomUser.objects.all().count()}
        return Response(nbs_user)


""" Manages creation's subscribe """


class CreateSubscribe(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, pseudoUser):
        serializer = SubscriptionSerializer(data=request.data)

        subscribe = Subscription.objects.filter(
            id_giving=request.user,
            id_receiving=request.data.get("id_receiving", "")
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
                id_receivin=request.data.get("id_receiving", "")
            ).count()
            return Response(serializer.data)


""" Manages all informations of user """


class GetAllInfoUser(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, idUser):
        user = CustomUser.objects.filter(id=idUser)

        CustomUser.info_user = {
            "nbs_gold_likes": user[0].likearticle_set.filter(
                reaction=1
            ).count(),

            "nbs_folows": Subscription.objects.filter(
                id_receiving=user[0]
            ).count()
        }
        serializer = AllInfosUserSerializer(user, many=True)
        return Response(serializer.data)


""" Manages endpoints to research user """


class ResearchUser(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, userSearch):
        user = CustomUser.objects.filter(username__icontains=userSearch)[:16]
        serializer = ResearchUserSerializer(user, many=True)
        return Response(serializer.data)


""" Shows whether the user is already subscribed or not """


class AlreadySubscribed(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, idReceiving):
        already_sub = {
            "already_sub": Subscription.objects.filter(
                id_giving=request.user,
                id_receiving=idReceiving,
                ).count()
        }

        return Response(already_sub)
