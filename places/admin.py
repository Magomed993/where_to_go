from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


class PlaceInline(SortableStackedInline):
    model = Image
    fields = [
        'img',
        'num',
        'get_preview'
    ]
    readonly_fields = [
        'get_preview'
    ]
    extra = 0

    def get_preview(self, obj):
        return format_html(
            '<img src="{0}" style="max-width: {1}; max-height: {1}">',
            obj.img.url,
            '200px',
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]
    search_fields = [
        'title'
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'place'
    ]
