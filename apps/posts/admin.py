from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at', 'categories', 'tags')
    inlines = [CommentInline]
    filter_horizontal = ('categories', 'tags')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('post__title', 'author__user__username', 'content')
    list_filter = ('created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
