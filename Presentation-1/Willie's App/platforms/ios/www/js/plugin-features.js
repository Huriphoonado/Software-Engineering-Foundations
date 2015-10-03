// Willie Payne
// Contains a set of functions to access device features

// Camera
function cameraSuccess(imageData) {
    var image = document.getElementById('myImage');
    image.src = "data:image/jpeg;base64," + imageData;
}

function cameraFail(message) {
    alert('Failed because: ' + message);
}

function useCamera() {
  navigator.camera.getPicture(cameraSuccess, cameraFail, { quality: 50,
    destinationType: Camera.DestinationType.DATA_URL
  });
}

// Geolocation
var geoSuccess = function(position) {
    alert('Latitude: '          + position.coords.latitude          + '\n' +
          'Longitude: '         + position.coords.longitude         + '\n' +
          'Altitude: '          + position.coords.altitude          + '\n' +
          'Accuracy: '          + position.coords.accuracy          + '\n' +
          'Altitude Accuracy: ' + position.coords.altitudeAccuracy  + '\n' +
          'Heading: '           + position.coords.heading           + '\n' +
          'Speed: '             + position.coords.speed             + '\n' +
          'Timestamp: '         + position.timestamp                + '\n');
};

function geoError(error) {
    alert('code: '    + error.code    + '\n' +
          'message: ' + error.message + '\n');
}

function getLocation() {
  navigator.geolocation.getCurrentPosition(geoSuccess, geoError);
}

// Accelerometer
function accelSuccess(acceleration) {
    alert('Acceleration X: ' + acceleration.x + '\n' +
          'Acceleration Y: ' + acceleration.y + '\n' +
          'Acceleration Z: ' + acceleration.z + '\n' +
          'Timestamp: '      + acceleration.timestamp + '\n');
};

function accelError() {
    alert('Accelerometer Error!');
};

function getAccel() {
  navigator.accelerometer.getCurrentAcceleration(accelSuccess, accelError);
}

// Contacts
function contactsSuccess(contacts) {
    alert('Found ' + contacts.length + ' contacts.');
};

function contactsError(contactError) {
    alert('Contacts Error!');
};

function getContacts() {
  var options = new ContactFindOptions();
  options.filter   = "";
  options.multiple = true;
  options.desiredFields = [navigator.contacts.fieldType.id];
  var fields = [navigator.contacts.fieldType.displayName, navigator.contacts.fieldType.name];
  navigator.contacts.find(fields, contactsSuccess, contactsError, options);
}