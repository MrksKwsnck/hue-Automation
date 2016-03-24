hue-Automation
==============

Controlling Philips hue lights by Nintendo's Wiimote and Bluetooth (BLE) beacon
events.


About
-----

The goal of this project is to control the *Philips hue* lights (color,
brightness etc.) with *Nintendo Wiimote* controllers. In a further step also
Bluetooth beacon events ([BLE][0]) shall trigger the state of the lights. This
project shall be realized on a *Raspberry Pi* platform running the *Raspbian
Jessie* Linux as operating system.


Prerequisites
-------------

For all this challenges to become realized, concrete software prerequisites need
to be met.


### Bluetooth ###

To establish a connection with a Wiimote the [Bluetooth stack][3] is needed.
Install the **bluez**-4.101 or newer (**bluez-5.0** or newer recommended)
package, as this versions have modern support for Wiimotes.

```bash
# Raspbian Jessie / Ubuntu Trusty Tahr
sudo apt-get install bluetooth

# Otherwise
sudo apt-get install bluez
```


### XWiimote ###

To be able to read the input from a Wiimote the [XWiimote][1] package is needed.
Supported by the **Linux kernel** 3.1 or newer (**3.11** or newer recommended)
it provides user space utilities for the Wiimote kernel driver.

```bash
sudo apt-get install xwiimote
```


Setting up
----------

### Pairing Wiimotes ###

The tricky part is to successfully pair a Wiimote with the Bluetooth adapter and
establish a connection, which also re-establishes itself automatically. For this
to accomplish a detailed [article at the ArchWiki][2] is provided.

**Summary:** You might have to call `sudo modprobe hid-wiimote` to load the
XWiimote driver manually. The pairing process must be initialized by the *red
sync button* near the batteries. And there is a very short time span to issue
the *connect* command right after the pairing succeded, so the automatic
re-establishment of the connection may work.


Further reading
---------------

* [hue Developer Program](http://www.developers.meethue.com/) - Official Philips
hue API.
* [Wiimote](http://wiibrew.org/wiki/Wiimote) *at WiiBrew* - Wiki with detailed
informations about the hardware and software of Wiimotes.

[0]:  https://en.wikipedia.org/wiki/Bluetooth_low_energy  "Bluetooth Low Energy"
[1]:  https://dvdhrm.github.io/xwiimote/  "Linux kernel driver for Wiimotes"
[2]:  https://wiki.archlinux.org/index.php/XWiimote "Usage of XWiimote"
[3]:  http://www.bluez.org/ "Official Linux Bluetooth protocol stack"
