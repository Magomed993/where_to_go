from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from catalog.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
              },
              "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "static/places/moscow_legends.json"
              }
            }
        )

    context = {
      'places':
        {
          "type": "FeatureCollection",
          "features": features
        }
    }
    return render(request, 'index.html', context)


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    absolute_url = [photo.image.url for photo in place.images.all()]
    json_place = {
      'title': place.title,
      'imgs': absolute_url,
      'description_short': place.short_description,
      'description_long': place.long_description,
      'coordinates': {
        'lat': place.lat,
        'lng': place.lng,
      }
    }
    return JsonResponse(json_place, json_dumps_params={'ensure_ascii': False, 'indent': 4})
