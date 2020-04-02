from django.contrib import admin

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Track, TrackAdmin)
