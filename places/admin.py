from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from .models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    fields = ['image', 'get_preview']
    extra = 1
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-width: 200px; max-height: 200px">', obj.image.url)

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
