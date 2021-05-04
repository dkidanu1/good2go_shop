console.log("LOADING MAPS.JS")
mapboxgl.accessToken = 'pk.eyJ1IjoiZGsxMjMzNDU1MzQzNCIsImEiOiJja252ZXRyc24wNHk3Mm9wbTF6NTYwNDRsIn0.1H5llGIQ0fJGyXovrPh0PA';
var map = new mapboxgl.Map({
container: 'map', // container id
style: 'mapbox://styles/mapbox/streets-v11', // style URL
center: [18.06913, 59.33301], // starting position [lng, lat]
zoom: 7, // starting zoom
width: '100px'
});

// Set options
var marker = new mapboxgl.Marker({
    color: "#FFFFFF",
    draggable: true
  }).setLngLat([18.0614, 59.3323])
  .addTo(map);