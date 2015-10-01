## Getting Started

### Installation

PhoneGap supports two interfaces for creating applications:

* Desktop App which can be downloaded and easily installed from [here](http://docs.phonegap.com/getting-started/1-install-phonegap/desktop/).

[PhoneGapInstaller.png]

* Command Line Interface - (Thorough instructions also found [here](http://docs.phonegap.com/getting-started/1-install-phonegap/cli).)

In order to install the Command Line Interface, first you will want to make sure you have [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/) installed. Then, type the following:

```
npm install -g phonegap@latest
```

Or in case you need root privilages:

```
sudo npm install -g phonegap@latest
```

Once that completes, to make sure you have PhoneGap correctly installed, type:

```
phonegap
```

And you should see a list of available commands:

```
Usage: phonegap [options] [commands]

Description:

  PhoneGap command-line tool.

Commands:

  help [command]       output usage information
  create <path>        create a phonegap project
  build <platforms>    build the project for a specific platform
  install <platforms>  install the project on for a specific platform
  run <platforms>      build and install the project for a specific platform
  platform [command]   update a platform version
  plugin [command]     add, remove, and list plugins
  template [command]   list available app templates
  info                 display information about the project
  serve                serve a phonegap project
  version              output version number
  ............................
  ............................
```

Type the following to check the version,

```
phonegap version
5.3.6
```

And as of current writing, the latest version of PhoneGap is 5.3.6.

In case you have issues with the download, the [npm page for PhoneGap](https://www.npmjs.com/package/phonegap) has some common errors and solutions listed.

### Getting the Developer App Working with the Desktop Interface

First, you will need to download the PhoneGap mobile app for your device ([iOS](https://itunes.apple.com/app/id843536693), [Android](https://play.google.com/store/apps/details?id=com.adobe.phonegap.app), [Windows Phone](https://www.microsoft.com/en-us/store/apps/phonegap-developer/9wzdncrdfsj0)). The PhoneGap Mobile app enables developers to work locally and see changes instantaneously on their device without recompiling or reinstalling the app. The app also provides access to device APIs.

Open up the Desktop PhoneGap application and click the "+" sign in the top right corner to create a new app.

[Setup1.png Image]

Provide a name, ID, and location and then click "Create Project."

[Setup2.png Image]

Click the play button to make sure the server is running and take note of the address.

[Setup3.png Image]

Open up the mobile app on your device and type in the server address shown in the Desktop App.

[Setup4.png Image]

If everything goes according to plan you should see the PhoneGap logo and the blinking text, "DEVICE IS READY."

[Setup5.png Image]

Finally, within your application directory open up index.html. (In my case it is found in Willie\'s\ App/www/index.html.) Any changes you make and save within this document should appear instantly on your device. In this example, I have changed the text within the header.

[Setup5.png Image]

### Getting the Developer App Working with the Commandline Interface
