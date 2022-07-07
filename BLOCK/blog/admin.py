from django.contrib import admin

from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ("author", "image", "desc")
    search_fields = ["author"]


admin.site.register(Post, PostAdmin)
