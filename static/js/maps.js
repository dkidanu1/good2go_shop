var mymap = L.map('map').setView([59.3149, -18.0721], 13);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 16,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZGsxMjMzNDU1MzQzNCIsImEiOiJja252Y2xyaXcwNTg2MnB0Z2ZiOHdqNnB4In0.o2kPUM_qMpuLPwPYo_cXEA'
}).addTo(mymap);
    var marker = L.marker([59.3149,18.0721]).addTo(mymap);
    marker.bindPopup("<b>We are located here!</b>").openPopup();