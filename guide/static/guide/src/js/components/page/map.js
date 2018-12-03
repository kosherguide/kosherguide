$(document).ready(function(){

    const jsonCoordinates = $('#json-coordinates').text();
    if (jsonCoordinates !== '') {
        var coordinates = JSON.parse(jsonCoordinates);
    }

    if ($('#map').length > 0 && !$('#map').is('.mapPage')) {
        mapboxgl.accessToken = 'pk.eyJ1Ijoia29zaGVyZ3VpZGUiLCJhIjoiY2prOWtveHp5MjBibjNxbWVkanMzY284dyJ9.bKvK0jtXCghJF_YJXa2G_Q';
        // This adds the map to your page
        var map = new mapboxgl.Map({
            container: 'map',
            // style URL
            style: 'mapbox://styles/kosherguide/cjmamaw1e1wym2smifi4u365a',
            // initial position in [lon, lat] format
            center: [coordinates.lng, coordinates.lat],
            // initial zoom
            zoom: 17
        });
        map.on('load', function (e) {
            // Add the data to your map as a layer
            map.addLayer({
                id: 'locations',
                type: 'symbol',
                // Add a GeoJSON source containing place coordinates and information.
                source: {
                    type: 'geojson',
                    data: {
                        "type": "FeatureCollection",
                        "features": [{
                            "type": "Feature",
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    coordinates.lng,
                                    coordinates.lat
                                ]
                            },
                            "properties": {}
                        }]
                    }
                },
                layout: {
                    'icon-image': 'restaurant-15',
                    'icon-allow-overlap': true,
                }
            });
        });
    }
});