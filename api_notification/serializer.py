from rest_framework import serializers
from user.models import Notification

""" Serializer for all notification """


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
