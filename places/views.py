from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        place.lng,
                        place.lat
                    ]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse(
                        'places',
                        kwargs={
                            'place_id': place.id
                        }
                    )
                }
            }
        )
    context = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(
        request,
        'index.html',
        context
    )


def places(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related(
                'images',
        ),
        pk=place_id
    )
    place_details = {
        'title': place.title,
        'imgs': [image.img.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long':  place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(
        place_details,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4
        }
    )
