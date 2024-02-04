# Kodi Autoplay Addon


## Introduction

This Addon is a Service useful to start at kodi boot another Addon


## Configuration

In Setting Page 2 items can be configured:

1. **Startup Addon**: choose an Addon to start ad Kodi boot (only Addon of *Script* type are allowed)
2. **Start Addon**: useful to test start of selected Addon (works only if addon is Enabled)

If you want disable automatic startup of selected Addon, use *Disable* Button in this Addon Page


## Compatibility

This Addon was tested on following platfoms (see branch compatibility on GitHub):
|   Kodi version  |       Distribution        |             HW             | Works | Branch | Notes |
| :-------------: | :-----------------------: | :------------------------: | :---: | :----: | :---- |
| Kripton - 17.6  | LibreELEC-RPi2.arm-8.2.5  | RasPi v1.2 model B+        |   Y   |  py2   |       |
| Leia - 18.9     | LibreELEC-RPi2.arm-9.2.6  | RasPi v1.2 model B+        |   Y   |  py2   |       |
| Matrix - 19.5   | LibreELEC-RPi4.arm-10.0.4 | RasPi v4 model B with 4GB  |   Y   |  py3   |       |
| Nexus - 20.3    | LibreELEC-RPi4.arm-11.0.6 | RasPi v4 model B with 4GB  |   Y   |  py3   |       |
| Nexus - 20.3    | LibreELEC-RPi5.arm-11.0.6 | RasPi v5 with 4GB          |   Y   |  py3   |       |


If anyone tests this Addon on other HW platforms / SW distribution, I'll insert into list


## Installation

Unless this addon was not included in a Kodi repository, must be installed manually.
To do so:
1. download this github repository as .zip
2. transfer file on host with Kodi (via network, USB memory, etc.)
3. in addon section choose "Install from .zip file" and browse file location
   (remember - if not asked - to enable installation of .zip addon from Settings -> Addon -> unknown source)


## Localization

If you want to add other localizations, you're welcome!
(send me `string.po` file and Addon description in addon.xml or do a Pull Request)


## Credits

Thanks to indication on pages:

* [Kodi Autoexec Service discussion on GitHub](https://github.com/xbmc/xbmc/pull/18356)
* [Kodi Autoexec Service HOW-TO](https://kodi.wiki/view/Autoexec_Service)
