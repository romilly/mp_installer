# Raspberry Pi Pico MicroPython installer

This installs MicroPython on a Raspberry Pi Pico/PicoW from the command line.

This **only works on Linux** and I do not have the hardware to port/test it to Windows or Mac/OS.

This software has had limited testing.

**Make sure that you have backups of any Pico files you want to keep before using it!**

## Installation

Clone this repository into a directory of your choice.

## Usage

Make sure that installer.py is executable.
From the project root, run

`installer.py [nuke]`

This will install the `rp2-pico-w-latest.uf2` MicroPython file from the uf2 subdirectory to an attached Pico or Pico W.

The optional `nuke ` argument will _nuke_ (delete) the entire Pico file system before installing MicroPython.
