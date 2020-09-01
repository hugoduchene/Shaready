from user.models import Notification, CustomUser

""" Manages the creation of notifications """


class ManageNotification():

    def create_notification(self, user_giving, pseudoUser, type):
        Notification(
            id_giving=user_giving,
            id_receiving=CustomUser.objects.get(username=pseudoUser),
            type_notification=type
        ).save()
