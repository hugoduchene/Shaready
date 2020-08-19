from rest_framework import serializers
from user.models import Subscription, CustomUser

class SubscriptionSerializer(serializers.ModelSerializer):
    nbs_follows = serializers.SerializerMethodField()
    
    def get_nbs_follows(self, obj):
        return obj.nbs_follows
    
    class Meta:
        model = Subscription
        fields = ('id_receiving', 'nbs_follows')

class AllInfosUserSerializer(serializers.ModelSerializer):
    info_user = serializers.SerializerMethodField()

    def get_info_user(self, obj):
        return obj.info_user
    
    class Meta:
        model = CustomUser
        fields = ('image_profile', 'username','info_user',)

class ResearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'image_profile', 'id')