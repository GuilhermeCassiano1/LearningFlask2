function initMap() {
    const restrictedBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(39.537064704469685, -119.81803893571075),  // Southwest corner of NYC
        new google.maps.LatLng(39.55024426280125, -119.81330216925673)   // Northeast corner of NYC
    );

    const mapStyles = [
        {
            featureType: "all",
            elementType: "labels",
            stylers: [{ visibility: "off" }]  // Hides all labels
        },
    ];


    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 39.54200731395531, lng: - 119.81499098680625 },
        zoom: 17,
        minZoom: 15,
        maxZoom: 20,
        restriction: {
            latLngBounds: restrictedBounds,
            strictBounds: false,
        },
        styles: mapStyles 
    });

    const tourStops = [
        { position: { lat: 39.54360464344734, lng: -119.81512379814838 }, title: "KC" },
        { position: { lat: 39.5400138786115, lng: -119.81460881399342 }, title: "Ansari Business" },
        { position: { lat: 39.53900032267345, lng: -119.81252741989516 }, title: "DMSC" },
        { position: { lat: 39.53999962488407, lng: -119.81330075020244 }, title: "SEM" },
        { position: { lat: 39.53980160266187, lng: -119.81196528367359 }, title: "WPEB" },
    ];

    const infoWindow = new google.maps.InfoWindow();

    tourStops.forEach(({ position, title }, i) => {
        const marker = new google.maps.Marker({
            position,
            map,
            title: `${i + 1}. ${title}`,
        });

        marker.addListener('click', function () {

            window.location.href = "/L&F";

        });
    });
}

window.onload = function () {
    initMap();
};

