KGclimate-django
================

A Django app that accepts and returns JSON arrays, mapping latitude and longitude coordinates to a Köppen-Geiger climate classification.

Classification details and data sets can be found here:
http://koeppen-geiger.vu-wien.ac.at/

See models.py for database schema. An example data set, with the most recently (1976 - 2000) observed climate class coordinates, is available in ASCII format in the root of this hub.

To request a climate_class, send a JSON array (via GET or POST) with two key-values, 'latitude' and 'longitude'. A JSON array with a single key-value, 'class', will be returned. 'Class' value is null if input is incomplete or improperly formatted.

Once the app is running, JQuery and JQuery-JSON (for example) can be used to interact with it: 
$.ajax({
    url: 'URL/pointing/to/KGclimate/', 
    type: 'POST', contentType: 'application/json; charset=utf-8', 
    data: $.toJSON({ lat: -89.75, lng: -179.75 }), 
    dataType: 'json', 
    success: function(data){ 
            alert(data['class']);
        }
    });