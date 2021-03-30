from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "created_time")
    search_fields = ("title", "post_name")
    list_filter = ("title", "created_time")
    readonly_fields = ("post_name", "title")
    fieldsets = (
        ("posts context", {"fields": (("post_name", "title"),)}),
        ("posts text", {"fields": (("text"),)}),
    )

# admin.site.register(Post)