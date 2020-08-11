from api_articles.serializers import ArticleSerializer
from django.db.models import Count

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
    