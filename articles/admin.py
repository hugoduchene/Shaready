from django.contrib import admin
from articles.models import (
    Article,
    Categories,
    LikeArticle,
    Comment,
    LikeComment,
)
# Register your models here.

admin.site.register(LikeComment)
admin.site.register(Comment)
admin.site.register(LikeArticle)
admin.site.register(Categories)
admin.site.register(Article)
