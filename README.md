# Raspberry Pi Pico MicroPython installer

This installs MicroPython on a Raspberry Pi Pico/PicoW from the command line.

This **only works on Linux** and I do not have the hardware to port/test it to Windows or Mac/OS.

This software has had limited testing.

**Make sure that you have backups of any Pico files you want to keep before using it!**

## Installation

Clone this repository into a directory of your choice.

## Usage

Make sure that mp-installer.py is executable.
From the project root, run

`./mp-installer.py <uf2 file> [nuke]`

This will install the MicroPython file whose path is <uf2 filew> to an attached Pico or Pico W.
The optional `nuke ` argument will _nuke_ (delete) the entire Pico file system before installing MicroPython.

So if I change to the project root and type 
`./mp-installer.py ~/Downloads/pi-pico/rp2-pico-w-20220727-unstable-v1.19.1-216-g45ab801c3.uf2`
that will leave the Pico filesystem untouched and install the nightly build for the Pico W from 27 July 2022.

