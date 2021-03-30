from django.contrib import admin
from accounts.models import ProfileModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ("user__username", "created_time", "image")
    list_display = ("user", "created_time", "image")
    search_fields = ("user__username", "timestamp")
    fieldsets = (
        ("fieldsets", {
            "fields": (("user", "image"),)
        }),
    )

# admin.site.register(ProfileModel)