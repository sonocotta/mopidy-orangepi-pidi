****************************
Mopidy-OrangePi-PiDi
****************************

Mopidy extension for displaying song info and album art using pidi display plugins.

Installation
============

Install by running::

    pip3 install Mopidy.OrangePi.Pidi

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<https://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-PiDi to your Mopidy configuration file::

    [orangepi-pidi]
    enabled = true
    display = opi.st7789

This example uses st7789 provided by OrangePi.PidiPlugins

Credits
=======

- Original author: `Phil Howard <https://github.com/pimoroni>`__
- Current maintainer: `Phil Howard <https://github.com/pimoroni>`__
- `Contributors <https://github.com/pimoroni/mopidy-pidi/graphs/contributors>`_
