from api_comments.serializer import CommentSerializer
from django.db.models import Count
from user.models import Notification

class AllDataComment():
    
    def get_all_infos_comment(self, objects):
        for obj in objects:
            nbs_likes = obj.likecomment_set.values(
                'reaction_comment'
            ).annotate(
                total=Count('reaction_comment')
            )
            
            obj.nbs_likes = {v['reaction_comment']:v['total'] for v in nbs_likes}
            obj.info_user = {
                "photo" : str(obj.id_user.image_profile),
                "pseudo" : obj.id_user.username
            }

        serializer = CommentSerializer(objects, many=True)
        return serializer

    def create_notification(user_giving, pseudoUser, type):
        create_notification = Notification(
            id_giving=user_giving, 
            id_receiving=CustomUser.objects.get(username=pseudoUser),
            type_notification= type
        ).save()
