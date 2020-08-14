from api_articles.serializers import ArticleSerializer
from django.core.paginator import Paginator
from django.db.models import Count
from user.models import Notification, CustomUser

class AllDataArticle():
    
    def get_all_infos(self, objects):
        for obj in objects:
            nbs_likes = obj.likearticle_set.values(
                'reaction'
            ).annotate(
                    total=Count('reaction')
            )
            
            obj.nbs_likes = {v['reaction']:v['total'] for v in nbs_likes}
            obj.info_user = {
                "photo" : str(obj.id_user.image_profile),
                "pseudo" : obj.id_user.username
            }

        serializer = ArticleSerializer(objects, many=True)
        return serializer
    
    def pagination_objects(self, objects, idPage):
        pagination = Paginator(objects, 10)
        objects_page = pagination.get_page(idPage).object_list

        return objects_page
    
    def create_notification(self, user_giving, pseudoUser, type):
        create_notification = Notification(
            id_giving=user_giving, 
            id_receiving=CustomUser.objects.get(username=pseudoUser),
            type_notification= type
        ).save()
