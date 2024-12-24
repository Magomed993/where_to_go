from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('places', kwargs={'place_id': place.id})
                }
        })
    context = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, 'index.html', context)


def places(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    details_json = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long":  place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(details_json, json_dumps_params = {"ensure_ascii": False, 'indent': 4})
