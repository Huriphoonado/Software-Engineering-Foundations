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

Installing first-party plugins may be done with the ```phonegap plugin add ``` command or alternatively the ```cordova plugin add``` command. For example, say you want your app to be able to take pictures via the device's camera. You would navigate to your PhoneGap project directory and run the following commands to add the plugin and check to make sure it has been added:

```
$ phonegap plugin add cordova-plugin-camera
Fetching plugin "cordova-plugin-camera" via npm

$ phonegap plugin list
cordova-plugin-camera 1.2.0 "Camera"
cordova-plugin-whitelist 1.0.0 "Whitelist"
```

Later, if you decide you do not need to use the camera in your application, you can easily remove it:

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

### Implementing Some Device Features
