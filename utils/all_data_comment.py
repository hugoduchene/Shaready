from api_comments.serializer import CommentSerializer
from django.db.models import Count

""" Manages all the information that the frontend needs for displaying comments """


class AllDataComment():

    def get_all_infos_comment(self, objects):
        for obj in objects:
            nbs_likes = obj.likecomment_set.values(
                'reaction_comment'
            ).annotate(
                total=Count('reaction_comment')
            )

            obj.nbs_likes = {v['reaction_comment']: v['total'] for v in nbs_likes}
            obj.info_user = {
                "photo": str(obj.id_user.image_profile),
                "pseudo": obj.id_user.username,
                "id_user_comment": obj.id_user.id,
            }

        serializer = CommentSerializer(objects, many=True)
        return serializer
