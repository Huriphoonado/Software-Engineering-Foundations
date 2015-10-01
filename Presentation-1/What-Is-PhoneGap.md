## What is PhoneGap Exactly and How Does it Work?

### Hybrid Apps
PhoneGap enables the development of so-called "hybrid apps," apps built with a combination of web technologies that are then wrapped inside a native container and distributed as native applications. Hybrid apps are run via a mobile platform's WebView, essentially a browser window configured to run fullscreen. Hybrid apps may contain native ui and web elements for example with navigation and transitions built natively while webviews are used for most of the content.

Most hybrid apps leverage Apache Cordova, a platform containing a set of Javascript APIs to access device capabilities via plug-ins built natively. Cordova was initially named PhoneGap, but now PhoneGap is a distribution of Cordova containing additional tools that tie into other Adobe services. (Check out this article: [PhoneGap, Cordova, and what’s in a name?](http://phonegap.com/2012/03/19/phonegap-cordova-and-what’s-in-a-name/))

### Differences Between Types of Apps

(Summary of this [helpful article on the PhoneGap Blog](http://phonegap.com/blog/2015/03/12/mobile-choices-post1/).)

| Native Mobile Apps                 | Hybrid Mobile Apps                 | Mobile Web Apps                    |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| Built for Specific OS              | Built with web technologies        | Built with web technologies        |
| Installed to the device            | Installed to the device            | Accessed via device web browser    |
| All native controls and APIs       | Accesses native APIs               | Little access to native features   |
| Distributed on app marketplace     | Distributed on app marketplace     | Not distributed on app marketplace |
| No dependencies on a container     | Run in an embedded web browser     | Served by a web server             |
| Offline capable                    | Offline capable                    | Not Offline capable                |

### Examples of Hybrid Apps

