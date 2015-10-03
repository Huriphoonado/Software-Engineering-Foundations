## What is PhoneGap Exactly and How Does it Work?

### Hybrid Apps
PhoneGap enables the development of so-called "hybrid apps," apps built with a combination of web technologies that are then wrapped inside a native container and distributed as native applications. Hybrid apps are run via a mobile platform's WebView, essentially a browser window configured to run fullscreen. Hybrid apps may contain a mix of native ui and web elements. For example, navigation and transitions may be built natively while webviews are used for most of the content. Well-made hybrid apps [should be largely indistinguishable from their native equivalents](http://developer.telerik.com/featured/what-is-a-hybrid-mobile-app/).

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

#### [Basecamp](https://basecamp.com)

A great example of a hybrid mobile app is Basecamp, largely becuase David Heinemeier Hansson (the creator of Ruby on Rails) and his team [blogged extensively on the development of the app](https://signalvnoise.com/posts/3743-hybrid-sweet-spot-native-navigation-web-content). Basecamp is a project management app enabling team members to communicate and check in on various projects. Hansson describes the benefits of the hybrid approach as far outweighing the challenges (which included dealing with webview integration and handling the loading phase.) Since the controllers and models powering the web version of the app are the same as in the mobile clients, features need only be implemented once, and since much of the features are served from a server, bug fixes and updates can be delivered without going through Apple's approval cycle. Overall, Hansson argues that a majority of information delivering applications can be delivered using the hybrid approach.

#### [Khan Academy](https://www.khanacademy.org)

Khan Academy's hybrid moble app is built by John Resig (the creator of JQuery). The app is a mobile learning platform enabling users to watch videos and read explanations on a variety of topics, work on interactive exercises, and sync their progress to the Khan Academy Website.

Other large-scale hybrid apps include Instagram, Yelp, Twitter, and Evernote. PhoneGap also [showcases a collection of apps](http://phonegap.com/app/) built with its platform.

#### [Get Started with PhoneGap](https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/Getting-Started.md)

#### [Go to Previous Page](https://github.com/Huriphoonado/Software-Engineering-Foundations/blob/master/Presentation-1/README.md)
