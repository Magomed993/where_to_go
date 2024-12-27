import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('places/<int:place_id>/', views.places, name='places'),
    path('tinymce/', include('tinymce.urls')),
    path('__debug__', include(debug_toolbar.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


