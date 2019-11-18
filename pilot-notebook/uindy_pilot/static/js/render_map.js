/**
 * All Map script functions 
 * Ziang Jia
 */

// Marker by facility longitude and latitude

function markerMap(){
	var myLatLng = {
			lat: Number(document.getElementById("lat").value), 
			lng: Number(document.getElementById("lon").value)};
//	console.log(myLatLng)
	var map = new google.maps.Map(document.getElementById('map'), {
		center : myLatLng,
		zoom : 18,
		scrollwheel: false
	});
	// Create a marker and set its position.
	var marker = new google.maps.Marker({
	    map: map,
	    position: myLatLng,
	    title: 'My name is Marker'
	});
}

// Input longitude & latitude form map

function httpGet(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function toLatLng(){
	address = document.getElementById('id_address').value;
	city = document.getElementById('id_city').value;
	if(address !="" && city !=""){
		theURL = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address+' '+city+'&key=AIzaSyBoH7KJj9RyS3m8ln11DrER4T8aWK5907E'
		console.log(theURL)
		results = httpGet(theURL)
		myLatLng = jQuery.parseJSON(results)["results"][0]["geometry"]["location"]
		console.log(myLatLng)
		var map = new google.maps.Map(document.getElementById('map'), {
			center : myLatLng,
			zoom : 18,
			scrollwheel: false
		});
		// Create a marker and set its position.
		var marker = new google.maps.Marker({
		    map: map,
		    position: myLatLng,
		    title: 'My name is Marker'
		});
		document.getElementById('id_lat').value = myLatLng['lat']
		document.getElementById('id_lon').value = myLatLng['lng']
	}else{
		alert("Please input address or city")
	}
	return false
}

