from user.models import Notification, CustomUser

class  ManageNotification():

    def create_notification(self, user_giving, pseudoUser, type):
        create_notification = Notification(
            id_giving=user_giving, 
            id_receiving=CustomUser.objects.get(username=pseudoUser),
            type_notification= type
        ).save()