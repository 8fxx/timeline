
const locationMap = {
    'gma': { longlat: [4.208670781551609, 73.4889671528297], zoom: 14 },
    'addu': { longlat: [-0.6238956882415954, 73.15848904042501], zoom: 13 },
    'kfushi': { longlat: [6.623305718095354, 73.06890240297888], zoom: 15 }
  };
  
  const defaultLocation = { longlat: [0, 0], zoom: 10 };
  
  const selected = locationMap[loc] || defaultLocation;
  
  var map = L.map('map', { attributionControl: false }).setView(selected.longlat, selected.zoom);
  

// Add a tile layer (e.g., OpenStreetMap)
//https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}.png
//https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png
//https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png


L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png', {
    attribution: 'OSINT Interactive Map'
}).addTo(map);

function convertStringToInt(string) {
    // Check if the string contains only numbers.
    let hasOnlyNumbers = true;
    for (let i = 0; i < string.length; i++) {
        if (!isNaN(string[i])) {
            continue;
        } else {
            hasOnlyNumbers = false;
            break;
        }
    }

    // If the string contains only numbers, convert it to an int.
    if (hasOnlyNumbers) {
        return parseInt(string);
    } else {
        // If the string contains letters, do nothing.
        return null;
    }
}


const modal = document.querySelector('#modal')
const openModal = document.querySelector('.open-button')
const closeModal = document.querySelector('.close-button')
const para = document.querySelector('#para')
const submitbtn = document.querySelector('.submit-button')
const closebtn = document.querySelector('.close-button')
var latl, longl


// Add event listener for click events on the map
map.on('click', function getlonglat(e) {
    latl = e.latlng.lat;
    longl = e.latlng.lng;
    $('#modal').appendTo("body").modal('show');
    return latl, longl
});

submitbtn.addEventListener('click', function (event) {
    var title = document.querySelector('#title').value
    var description = document.querySelector('#description').value
    var selectedradio = document.getElementsByName('icon');

    for (i = 0; i < selectedradio.length; i++) {
        if (selectedradio[i].checked) {
            var test = selectedradio[i].value
        }
    }
    $.ajax({
        type: 'POST',
        url: '/add_pointer/',
        data: {
            'latitude': latl,
            'longitude': longl,
            'title': title,
            'description': description,
            'icon': test,
        },
        headers: {
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
        success: function (response) {
            if (response.success) {
                location.reload();
            } else {
                alert('Failed to add pointer.');
            }
        },
        error: function (xhr, status, error) {
            console.log(error);
            alert('An error occurred.');
        }
    });
});


document.addEventListener('click', function (event) {
    var target = event.target;
    let value1 = convertStringToInt(target.id)
    if (Number.isInteger(value1)) {
        $.ajax({
            url: '/delete_pointer/',
            method: 'POST',
            data: {
                "PointerID": target.id,
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
            mode: 'same-origin',
            success: function (response) {

                location.reload();
            },
            error: function (xhr, status, error) {

            }
        });
    }
});

closebtn.addEventListener('click', function (event) {
    $('#modal').modal('hide');
});

$('.closeModalBtn').click(function() {
    $('#modal').modal('hide');
  });











