from django.contrib import admin

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    fields = ["id", "points", "created_at"]
    list_display = ["id", "created_at"]
    readonly_fields = ["id", "created_at"]


admin.site.register(Track, TrackAdmin)
