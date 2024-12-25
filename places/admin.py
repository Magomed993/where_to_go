from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class PlaceInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview', 'num']

    def get_preview(self, obj):
        return format_html('<img src="{0}" width=auto height=200px />',
                           obj.img.url,
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
