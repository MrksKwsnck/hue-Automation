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

Afer you have succesfully paired a Wiimote, you can run the provided command
`sudo xwiishow 1` (where super user privileges are suggested and the number
argument identifies a Wiimote) to check whether all input is working properly.


### Install language bindings ###

For further development the language bindings [xwiimote-bindings][5] for the
[xwiimote][4] package are being needed. Get both packages directly from their
GitHub repositories, as you need to compile them yourself. To do so follow these
steps:

**NOTE:** The prefix is set to `$HOME/usr` for convenience. You will find all
the compiled files there beneath your home directory. That way the system does
not get messed up!

```
# Dependencies needed for Raspbian Jessie
sudo apt-get install automake autoconf libtool m4 libncurses5 libncurses5-dev libudev-dev swig libxwiimote2 libxwiimote-dev python-dev


############
# xwiimote #
############

# Clone the xwiimote project and change into its directory
git clone git@github.com:dvdhrm/xwiimote.git
cd xwiimote

# Prepare the project for compilation (this will take a while)
./autogen.sh --prefix=$HOME/usr

# Compile and install
make
make install


#####################
# xwiimote-bindings #
#####################

# Clone the xwiimote-bindings project and change into its directory
git clone git@github.com:dvdhrm/xwiimote-bindings.git
cd xwiimote-bindings

# Tell xwiimote-bindings where xwiimote can be found
export PKG_CONFIG_PATH=$HOME/usr/lib/pkgconfig

# Prepare the project for compilation (this will take a while)
./autogen.sh --prefix=$HOME/usr

# Compile and install
make
make install
```


### Test language bindings ###

Because xwiimote and the language bindings were installed beneath the prefixed
`$HOME/usr` path, you need to configure the dynamic linker *ldconfig*
appropriately. Otherwise the shared objects will not be found. To do so, add the
**expanded** prefix path (e.g. `/home/pi/usr/lib`) into the `/etc/ld.so.conf`
configuration file **before any other** path or include. After that reload the
shared library cache with: `sudo ldconfig` -- Alternatively, if you do not want
to change the dynamic linkers configuration, you can pass the prefix path with
the `LD_LIBRARY_PATH` environment variable to the Python interpreter.

Finally, the time has come to test the shipped example. For this it is necessary
to tell the Python interpreter where it can find the xwiimote module. The
simplest way is to preceed the Python interpreter with the environment variable
`PYTHONPATH`, which contains colon separated paths to modules.

```
sudo LD_LIBRARY_PATH=$HOME/usr/lib PYTHONPATH=$HOME/usr/lib/python2.7/site-packages python examples/python/xwiimote_test.py
```

**Hint:** For some access to the Wiimote hardware, super user privileges are
needed!

If all went well so far, you will see some status output and the Wiimote rumbles
shortly.


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
[4]:  https://github.com/dvdhrm/xwiimote  "Open Source Nintendo Wii Remote Linux Device Driver"
[5]:  https://github.com/dvdhrm/xwiimote-bindings "Language bindings for the xwiimote package"
