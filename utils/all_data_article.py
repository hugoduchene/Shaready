from api_articles.serializers import ArticleSerializer
from django.core.paginator import Paginator
from django.db.models import Count


""" Manages all the information that the frontend needs for the display of articles """


class AllDataArticle():

    def get_all_infos(self, objects):
        for obj in objects:
            nbs_likes = obj.likearticle_set.values(
                'reaction'
            ).annotate(
                    total=Count('reaction')
            )
            obj.nbs_comments = obj.comment_set.count()
            obj.nbs_likes = {v['reaction']: v['total'] for v in nbs_likes}
            obj.info_user = {
                "id_user": obj.id_user.id,
                "photo": str(obj.id_user.image_profile),
                "pseudo": obj.id_user.username
            }

        serializer = ArticleSerializer(objects, many=True)
        return serializer

    def pagination_objects(self, objects, idPage):
        pagination = Paginator(objects, 10)
        objects_page = pagination.page(idPage).object_list

        return objects_page
