# PhoneGap

## Introduction

##### PhoneGap is an open source and free framework (with some optional priced tools) enabling the creation of mobile apps across platforms using standard web APIs (HTML, CSS, Javascript).

Consider a small company that wishes to build an app and release it on a few of the mainstream mobile devices. With PhoneGap, rather than requring multiple teams or development cycles to produce a iOS version of the app with Objective C or Swift, an Android version with Java, and a Windows version with XAML and C#, the process may be streamilined with the bulk of the codebase for all versions of the app developed within the same languages. (Of course it is not that simple, but we will get to that later.)

### Advantages (Why Should We Care?)
1. Most importantly, PhoneGap shortens the development cycle for cross-platform mobile apps. Rather than developing two (or more) versions of the same app, the majority of code should remain the same across platforms.
2. There are less languages to learn and many programmers, including less-experienced programmers, already have experience building websites. PhoneGap makes app development much more accessible to new programmers and small teams.
3. PhoneGap supports many platforms including iOS, Android, Windows Phone, and Amazon Fire, and on those platforms PhonGap supports many device APIs including accelerometer, notifications, and camera.
4. PhoneGap provides a graphic user interface as well as a command line interface to support different developer preferences. Additionally, PhoneGap provides an alternative option to build and package apps via a [cloud service](https://build.phonegap.com).

### Disadvantages (When is PhoneGap the Wrong Tool?)
1. The main disadvantage is that PhoneGap apps are not built natively and thus are less responsive than native apps. In simple apps with basic CRUD (Create, Read, Update, Delete) functions, the interface may may feel slower or less comfortable, and more intensive apps such as 3d games may not be possible with PhoneGap.
2. Even though much of the code powering PhoneGap apps across platforms will be the same, each version of the app will require a different user interface matching each platform's specifications. (For example, Apple's substantial human interface guidelines may be found [here](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/) and Android's may be found [here](https://developer.android.com/design/index.html).) While PhoneGap apps may be developed and deployed faster than native apps, getting them to look and feel native may take significant work.
3. In order to access native device features (camera, accelerometer, etc.), PhoneGap relies on plug-ins. Plug-ins for certain features may be out-of-date, unreliable, or missing altogether especially when device operating systems are updating.

### Recommended PhoneGap Usage
PhoneGap is best for individuals or small teams who want to develop and release an app supporting two or more platforms with limited time that does not make use of extensive graphics or animation. PhoneGap may also work well in larger development teams for prototyping an app before working on the final native versions.

#### So what exactly is PhoneGap and how does it work?
