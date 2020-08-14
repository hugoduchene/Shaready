from rest_framework import serializers
from user.models import Notification

class NbsNotificationSerializer(serializers.ModelSerializer):
    nbs_notification = serializers.SerializerMethodField()
    
    def get_nbs_notification(self, obj):
        return obj.nbs_notification
    
    class Meta:
        model = Notification
        fields = ('nbs_notification',)

class AllDataNotificationSerializer(serializers.ModelSerializer):
    infos_user = serializers.SerializerMethodField()

    def get_infos_user(self, obj):
        return obj.infos_user
    
    class Meta:
        model = Notification
        fields = (
            'infos_user', 
            'type_notification',
            'read',
            'date_notification',
        )


