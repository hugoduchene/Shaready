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
    nbs_likes = serializers.SerializerMethodField()

    def get_nbs_likes(self, obj): 
        return obj.nbs_likes
    
    class Meta:
        model = LikeComment
        fields = ('reaction_comment', 'nbs_likes')

class CommentArticleSerializer(serializers.ModelSerializer):
    info_user = serializers.SerializerMethodField()

    def get_info_user(self, obj):
        return obj.info_user
    
    class Meta:
        model = Comment
        fields = ('content_comment', 'info_user')