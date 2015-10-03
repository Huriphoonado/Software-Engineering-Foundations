## Introduction to Cordova Plug-Ins

As has been briefly described before, really the core of PhoneGap is [Apache Cordova](https://cordova.apache.org), a set of device APIs allowing the developer to access native device functions with Javascript.

### Installing Cordova

In order to get Cordova type the following:

```
$ npm install -g cordova
```

Or, if you need root privileges:

```
$ sudo npm install -g cordova
```

Then type:

```
$ cordova
Synopsis

    cordova command [options]

Global Commands

    create ............................. Create a project
    help ............................... Get help for a command

Project Commands

    info ............................... Generate project information
    requirements ....................... Checks and print out all the requirements
                                            for platforms specified

    platform ........................... Manage project platforms
    plugin ............................. Manage project plugins

    prepare ............................ Copy files into platform(s) for building
    compile ............................ Build platform(s)
    clean .............................. Cleanup project from build artifacts

    run ................................ Run project
                                            (including prepare && compile)
    serve .............................. Run project with a local webserver
                                            (including prepare)

```

And finally, you may want to type:

```
$ cordova -v
5.3.3
```

As of current writing, the most up-to-date version is 5.3.3.

### Note on Cordova vs PhoneGap

The PhoneGap CLI is built on top of the Cordova CLI so all Cordova commands are supported by PhoneGap, but PhoneGap has additional features. Most commands can be called with ```phonegap ```, ```cordova ```, or even  ```phonegap cordova ```. In some cases though, the same command run via different CLIs may have different behaviors. (It is a bit confusing.) Check out [this page](http://docs.phonegap.com/references/phonegap-cli/cordova) for more information.

### Getting Cordova Plug-Ins

Cordova ships with a small set of APIs which which may be found in the [Cordova API Reference Guide](http://cordova.apache.org/docs/en/5.0.0/cordova_plugins_pluginapis.md.html#Plugin%20APIs). Third-party plug-ins may be searched through on [NPM](https://www.npmjs.com/search?q=ecosystem%3Acordova). 

Installing first-party plugins may be done with the ```phonegap plugin add ``` command or alternatively the ```cordova plugin add``` command. For example, say you want your app to be able to take pictures via the device's camera. You would navigate to your PhoneGap project directory and run the following commands to add the plugin and check to make sure it has been added. (The Whitelist plug-in controls which URLs the WebView itself can be navigated to.)

```
$ phonegap plugin add cordova-plugin-camera
Fetching plugin "cordova-plugin-camera" via npm

$ phonegap plugin list
cordova-plugin-camera 1.2.0 "Camera"
cordova-plugin-whitelist 1.0.0 "Whitelist"
```

Later, if you decide you do not need to use the camera in your application, you can easily remove it. In order to keep the size of your application as small as possible, you will want to remove anything you do not use:

```
$ phonegap plugin remove camera
Removing "cordova-plugin-camera"
```

However, in this case we'll keep the camera plug-in and let's go ahead and add a few more as well. (I'll use the ```cordova``` command to illustrate it does the same thing.)

```
$ cordova plugin add cordova-plugin-device-motion
Fetching plugin "cordova-plugin-device-motion" via npm

$ cordova plugin add cordova-plugin-contacts
Fetching plugin "cordova-plugin-contacts" via npm

$ cordova plugin add cordova-plugin-geolocation
Fetching plugin "cordova-plugin-geolocation" via npm

$ cordova plugin list
cordova-plugin-camera 1.2.0 "Camera"
cordova-plugin-contacts 1.1.0 "Contacts"
cordova-plugin-device-motion 1.1.1 "Device Motion"
cordova-plugin-geolocation 1.0.1 "Geolocation"
cordova-plugin-whitelist 1.0.0 "Whitelist"
```

### Accessing Native Device Functions with Cordova

Once they have been added to the plugins directory, it is easy to access device functionality with a set of Javascript functions. Using the PhoneGap mobile app to test your code enables use of device APIs whereas testing the code within a browser via localhost will not.

First things first, I've added a few buttons in www/index.html that when pressed will trigger functions in javascript.

```
<button class="topcoat-button--large" onclick="getContacts()">Count Contacts</button>
<button class="topcoat-button--large" onclick="useCamera()">Take Photo</button>
<button class="topcoat-button--large" onclick="getLocation()">Get Location</button>
<button class="topcoat-button--large" onclick="getAccel()">Accelerometer</button>
```

Then, in a new file www/js/plugin-features.js, I've written the following functions supporting the camera API, geolocation API, accelerometer API, and the contacts API. Each function requires success and failure callbacks, and each device feature is called via the ```navigator``` object. Failure functions may be called for a number of reasons most notably if the user does not give permission to the app to access the feature such as his/her location.

<img src=https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/images/AppScreen.PNG width="375" height="667" align="middle" />

#### Camera

The [camera API](https://www.npmjs.com/package/cordova-plugin-camera) enables a user to take a photo or retrieve a picture from the user's gallery. The developer may retrieve the image as base64 encoded image (which is shown below and is more useful if you are pushing the image to a database outside of the device) or a link to the image, and specify the quality of the image among other options.

```
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
```

#### Geolocation

The [geolocation API](https://www.npmjs.com/package/cordova-plugin-geolocation) provides information about the device's location including latitude, longitude, altitude, and speed. The following success function will simply trigger an alert displaying a lot of geolocation information.

```
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
```

<img src=https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/images/AppLocate.PNG width="375" height="667" align="middle" />

#### Accelerometer

The [accelerometer API](https://www.npmjs.com/package/cordova-plugin-device-motion) utilizes the device's motion sensor that may return continuous or discrete values pointing to the change in the device's movement relative to its position. (It's worth pointing out that this API currently has a build status of "failing.")

```
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
```

<img src=https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/images/AppAccel.PNG width="375" height="667" align="middle" />

The [contacts API](https://www.npmjs.com/package/cordova-plugin-contacts) enables a user to add a new contact to their directory or access contacts within their directory. When searching through a directory, the developer may specify what information to filter by (eg. all contacts named "Sam") as well as how many contacts to return. The following function simply counts how many contacts are stored within the user's directory.

#### Contacts

```
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
```

<img src=https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/images/AppContacts.PNG width="375" height="667" align="middle" />

Of course, there are many other plug-ins allowing access to the battery level, wifi status, vibration, etc, and Cordova [provides resources](http://cordova.apache.org/docs/en/5.0.0/guide_hybrid_plugins_index.md.html#Plugin%20Development%20Guide) to help you develop your own custom plugins. You will want to make sure that if a device feature is critical to your app that you read the documentation on it in the [API Guide](http://cordova.apache.org/docs/en/5.0.0/cordova_plugins_pluginapis.md.html#Plugin%20APIs) before committing to PhoneGap. Many plug-ins including the ones covered above have device specific quirks and capabilities. (For example, only the iOS camera API allows you to geotag photos.)

### Building your Application and Next Steps
