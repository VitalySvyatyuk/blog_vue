from django.contrib import admin

from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'edited',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'article', 'created',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
