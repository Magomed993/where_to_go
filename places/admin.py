from django.contrib import admin
from places.models import Place, Image


class PlaceInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
