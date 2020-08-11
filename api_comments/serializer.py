from rest_framework import serializers
from articles.models import (
    Comment,
    LikeComment,
)

class CommentSerializer(serializers.ModelSerializer):
    nbs_likes = serializers.SerializerMethodField()
    info_user = serializers.SerializerMethodField()
    
    def get_nbs_likes(self, obj): 
        return obj.nbs_likes
    
    def get_info_user(self, obj):
        return obj.info_user
    
    class Meta:
        model = Comment
        fields = '__all__'

class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = ('like_comment', 'dislike_comment')

class CommentArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content_comment',)