from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'comment_date',
    )


admin.site.register(Comment, CommentAdmin)
