from rest_framework import serializers
from user.models import Subscription, CustomUser

""" Serializer to manage subscription """


class SubscriptionSerializer(serializers.ModelSerializer):
    nbs_follows = serializers.SerializerMethodField()
    already_follow = serializers.SerializerMethodField()

    def get_already_follow(self, obj):
        return obj.already_follow

    def get_nbs_follows(self, obj):
        return obj.nbs_follows

    class Meta:
        model = Subscription
        fields = ('id_receiving', 'nbs_follows', 'already_follow')


""" Serializer to manage all information """


class AllInfosUserSerializer(serializers.ModelSerializer):
    info_user = serializers.SerializerMethodField()

    def get_info_user(self, obj):
        return obj.info_user

    class Meta:
        model = CustomUser
        fields = ('image_profile', 'username', 'info_user', 'id')


""" Serializer to manage user searches """


class ResearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'image_profile', 'id')
