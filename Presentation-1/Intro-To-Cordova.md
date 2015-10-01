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

The PhoneGap CLI is built on top of the Cordova CLI so all Cordova commands are supported by PhoneGap, but PhoneGap 

### Getting Cordova Plug-Ins

Cordova ships with a small set of APIs which which may be found in the [Cordova API Reference Guide](http://cordova.apache.org/docs/en/5.0.0/cordova_plugins_pluginapis.md.html#Plugin%20APIs). Third-party plug-ins may be searched through on [NPM](https://www.npmjs.com/search?q=ecosystem%3Acordova). 

Installing first-party plugins may be done with the ```phonegap plugin add ``` command or alternatively the ```cordova plugin add``` command. For example, say you want your app to be able to take pictures via the device's camera. You would navigate to your PhoneGap project directory and type the following:

```

```
