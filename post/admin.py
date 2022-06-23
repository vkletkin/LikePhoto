from django.contrib import admin
from .models import Post, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug", "author")
    search_fields = ("name", "slug",)
    list_filter = ("slug",)
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    list_display = ("group", "image", "rating")
    search_fields = ("group",)
    list_filter = ("group",)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
