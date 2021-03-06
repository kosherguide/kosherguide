$(document).ready(function() {
    const jsonStores = $('#json_stores').text();

    // This will let you use the .remove() function later on
    if (!('remove' in Element.prototype)) {
        Element.prototype.remove = function () {
            if (this.parentNode) {
                this.parentNode.removeChild(this);
            }
        };
    }

    mapboxgl.accessToken = 'pk.eyJ1Ijoia29zaGVyZ3VpZGUiLCJhIjoiY2prOWtveHp5MjBibjNxbWVkanMzY284dyJ9.bKvK0jtXCghJF_YJXa2G_Q';

    // This adds the map to your page
    var map = new mapboxgl.Map({
        container: 'map',
        // style URL
        style: 'mapbox://styles/kosherguide/cjmamaw1e1wym2smifi4u365a',
        // initial position in [lon, lat] format
        center: [37.612741, 55.773005],
        // initial zoom
        zoom: 14
    });

    var stores = JSON.parse(jsonStores);

    map.on('load', function (e) {
        // Add the data to your map as a layer
        map.addLayer({
            id: 'locations',
            type: 'symbol',
            // Add a GeoJSON source containing place coordinates and information.
            source: {
                type: 'geojson',
                data: stores
            },
            layout: {
                'icon-allow-overlap': true,
                "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
                "text-offset": [10, 10],
            }
        });

        // Initialize the list
        buildLocationList(stores);
    });

    // Add an event listener for when a user clicks on the map
    map.on('click', function (e) {
        // Query all the rendered points in the view
        var features = map.queryRenderedFeatures(e.point, {layers: ['locations']});

        if (features.length) {
            var clickedPoint = features[0];
            // 1. Fly to the point
            flyToStore(clickedPoint);

            // 2. Close all other popups and display popup for clicked store
            createPopUp(clickedPoint);

            // 3. Highlight listing in sidebar (and remove highlight for all other listings)
            var activeItem = document.getElementsByClassName('active');
            if (activeItem[0]) {
                activeItem[0].classList.remove('active');
            }

            // Find the index of the store.features that corresponds to the clickedPoint that fired the event listener
            var selectedFeature = clickedPoint.properties.address;

            for (var i = 0; i < stores.features.length; i++) {
                if (stores.features[i].properties.address === selectedFeature) {
                    selectedFeatureIndex = i;
                }
            }

            // Select the correct list item using the found index and add the active class
            var listing = document.getElementById('listing-' + selectedFeatureIndex);
            listing.classList.add('active');
        }
    });

    function flyToStore(currentFeature) {
        map.flyTo({
            center: currentFeature.geometry.coordinates,
            zoom: 15
        });
    }

    function createPopUp(currentFeature) {
        var popUps = document.getElementsByClassName('mapboxgl-popup');
        // Check if there is already a popup on the map and if so, remove it
        if (popUps[0]) popUps[0].remove();

        var popup = new mapboxgl.Popup({closeOnClick: false})
            .setLngLat(currentFeature.geometry.coordinates)
            .setHTML('<h3>' + currentFeature.properties.name + '</h3>' +
                '<h4>' + currentFeature.properties.address + '</h4>')
            .addTo(map);
    }

    function buildLocationList(data) {
        // Iterate through the list of stores
        for (i = 0; i < data.features.length; i++) {
            var currentFeature = data.features[i];
            // Shorten data.feature.properties to just `prop` so we're not
            // writing this long form over and over again.
            var prop = currentFeature.properties;

            // Select the listing container in the HTML and append a div
            // with the class 'item' for each store
            var listings = document.getElementById('listings');
            var listing = listings.appendChild(document.createElement('div'));
            listing.dataPosition = i;
            listing.className = 'item';
            listing.id = 'listing-' + i;


            var wrapper = listing.appendChild(document.createElement('div'));
            wrapper.className = 'wrapper';

            var pic = wrapper.appendChild(document.createElement('div'));
            pic.className = 'pic';

            // Изображение
            var img = pic.appendChild(document.createElement("div"));
            img.style.backgroundImage = 'url(' + prop.pic + ')';
            //img.setAttribute("src", prop.pic);
            var imgHtml = pic.appendChild(img);
            imgHtml.className = 'img';

            var mainDetail = wrapper.appendChild(document.createElement('div'));
            mainDetail.className = 'content';

            // Create a new link with the class 'title' for each store
            // and fill it with the store address
            var link = mainDetail.appendChild(document.createElement('a'));
            link.href = '/category/' + prop.sectionCode + '/' + prop.handle + '/';
            link.target = '_blank';
            link.className = 'title';
//        link.dataPosition = i;
            link.innerHTML = prop.name;

            // Create a new div with the class 'details' for each store
            // and fill it with the city and phone number
            var details = mainDetail.appendChild(document.createElement('div'));
            details.className = 'info';
            details.innerHTML = prop.country + ' &middot; ' + prop.city;

//        var link = mainDetail.appendChild(document.createElement('a'));
//        link.target = '_blank';
//        link.href = '/category/restaurants/' + prop.handle + '/';
//        link.className = 'more';
//        link.innerHTML = 'Подробнее';


//        if (prop.phone) {
//          details.innerHTML += ' &middot; ' + prop.phoneFormatted;
//        }

            listing.addEventListener('click', function (e) {
                // Update the currentFeature to the store associated with the clicked link
                var clickedListing = data.features[this.dataPosition];

                // 1. Fly to the point associated with the clicked link
                flyToStore(clickedListing);

                // 2. Close all other popups and display popup for clicked store
                createPopUp(clickedListing);

                // 3. Highlight listing in sidebar (and remove highlight for all other listings)
                var activeItem = document.getElementsByClassName('active');

                if (activeItem[0]) {
                    activeItem[0].classList.remove('active');
                }
//            this.parentNode.classList.add('active');
                this.classList.add('active');
            });
        }

        $('.scrollbar').customScrollbar();
    }
});