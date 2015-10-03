## Building Your App and Next Steps

### Building and Running a PhoneGap App

PhoneGap includes two tools for building your app: the Command Line Interface and [PhoneGap Build](https://build.phonegap.com) which compliles your app for you via a cloud service and maintains the most up-to-date SDKs. Since PhoneGap Build requires an account and money if you want to maintain more than one app, I will only cover the CLI.

First, you will want to tell PhoneGap what platforms you intend to deploy your app to. PhoneGap will automatically install the plugins you are using for each platform.

```
$ phonegap platform add android
Adding android project...

Creating Cordova project for the Android platform:

	Path: platforms/android
	Package: com.willie.app1
	Name: Willie's App
	Activity: MainActivity
	Android target: android-22

Copying template files...

Android project created with cordova-android@4.1.1

Installing "cordova-plugin-camera" for android

Installing "cordova-plugin-contacts" for android

Installing "cordova-plugin-device-motion" for android

Installing "cordova-plugin-geolocation" for android

Installing "cordova-plugin-whitelist" for android
```

You can also check at any time what platforms you have installed.

```
$ phonegap platform list
Installed platforms: android 4.1.1, ios 3.9.1
Available platforms: amazon-fireos, blackberry10, browser, firefoxos, osx, webos
```

Then, in order to build and install your app, run the following:

```
$ phonegap platform run ios
[phonegap] executing 'cordova platform run ios'...
[phonegap] completed 'cordova platform run ios'
```

Anytime you update the source code, you will need to run this command again.

From here on, you are mostly done with PhoneGap and get to learn how to use each SDK for the devices you intend to deploy to. (Luckily, most of the work has already been done for you with PhoneGap!) Cordova contains a set of [platform guides](http://docs.phonegap.com/en/edge/guide_platforms_index.md.html) providing information on setting up your development environment as well as solutions to common problems.

I have an iPhone, so in order to get the app running on my phone I will need XCode. (XCode may be downloaded from [here](https://developer.apple.com/xcode/).) Once XCode is installed, open it and navigate within your application directory to platforms/ios and find the file with type ".xcodeproj"

<img src=https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/images/OpenApp.png width="470" height="390" align="middle" />

Then, you will want to emulate your app using an iOS simulator. Select a device in the top left corner, click the play button, and if all goes according to plan you should see your app displayed on a virtual iPhone/iPad!

<img src=https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/images/EmulateApp.png width="761" height="548" align="middle" />

Finally, in order to run the app on your device, plug your device into your computer, select iOS device, and click play.

### Next Steps

As you can tell, this app does not do very much or look like a native iOS app. (It definitely would not pass Apple's review to make it onto the App Store!) PhoneGap does not provide tools for actually designing the app's interface. For that you will likely want to use a web framework. The following libraries are examples of tools you may wish to include within your project (in no particular order):
* [JQueryMobile](https://jquerymobile.com) is a web-framework for making responsive mobile websites. JQueryMobile however is very heavy.
* [Topcoat](http://topcoat.io) is a super lightweight css library developed by Adobe for fast web apps.
* [Backbone](http://backbonejs.org) is an MVC (Model View Controller) framework allowing for cleaner software architecture.
* [FastClick](https://github.com/ftlabs/fastclick) removes the 300 ms click delay in mobile browsers. Removing this delay is necessary for making a PhoneGap app feel native.
* [Ionic](http://ionicframework.com) is a brand-new open source SDK for creating hybrid apps with Cordova and Angular. (This may become a replacement to PhoneGap in the future.)

Finally, you will want to consider what blend of native controls and webviews you will want to use in order to make your app feel as fast and native as possible. PhoneGap provides iOS and Android guides [here](http://docs.phonegap.com/develop/1-embed-webview/ios/).
