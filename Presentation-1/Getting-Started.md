## Getting Started

### Installation

PhoneGap supports two interfaces for creating applications:

1. Desktop App which can be downloaded and easily installed from [here](http://docs.phonegap.com/getting-started/1-install-phonegap/desktop/).

[Image]

2. Command Line Interface - (Thorough instructions also found [here](http://docs.phonegap.com/getting-started/1-install-phonegap/cli).)

In order to install the Command Line Interface, first you will want to make sure you have [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/) installed. Then, type the following:

```
npm install -g phonegap@latest
```

Or in case you need root privilages:

```
sudo npm install -g phonegap@latest
```

Once that succeeds, in order to make sure you have PhoneGap correctly installed, type:

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
  .............................
```

Type 

```
phonegap version
5.3.6
```

And as of current writing, the newest version of PhoneGap is 5.3.6

In case you have issues with the download, the [npm page for PhoneGap](https://www.npmjs.com/package/phonegap) has some common errors and solutions listed.

### Getting the First App Working with the Desktop App
