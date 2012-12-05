from django.http import HttpResponse
from KGclimate.models import Coordinate
from KGclimate.functions import round_coordinate
import json

def index(request):
    if request.is_ajax():
        coordinates = json.loads(request.body)
        lat = coordinates.get('latitude', None)
        lng = coordinates.get('longitude', None)
        if lat > -90 and lat < 90 and lng > -180 and lng < 180:
            # Format coordinates
            lat = round_coordinate(lat)
            lng = round_coordinate(lng)
            # Query db and return
            coordinate = Coordinate.objects.get(latitude=lat, longitude=lng)
            return HttpResponse(json.dumps({ 'class': coordinate.climate_class.climate_class }), content_type='application/json')
        # Input didn't meet requirements
        return HttpResponse(json.dumps({ 'class': None }), content_type='application/json')
    # No input
    return HttpResponse("To request a climate_class, send a JSON array (via GET or POST) with two key-values, 'latitude' and 'longitude'. A JSON array with a single key-value, 'class', will be returned. 'Class' value is null if input is incomplete or unrecognized. Here is an example call with JQuery and JQuery-JSON: $.ajax({ url: '/tools/KGclimate/', type: 'POST', contentType: 'application/json; charset=utf-8', data: $.toJSON({ lat: -89.75, lng: -179.75 }), dataType: 'json', success: function(data){ alert(data['class']);} });")
