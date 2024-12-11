from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'get_preview', 'order']
    extra = 1
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-width: 200px; max-height: 200px">', obj.image.url)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
      ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  pass
