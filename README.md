RaspberryPi with UnicornHat
===========================
test project

About Unicorns - https://github.com/pimoroni/unicorn-hat


Installing OS
=============

 - Download Raspbian Jessie Lite from here https://www.raspberrypi.org/downloads/raspbian/
 - Write the downloaded image to a flash card
   https://www.raspberrypi.org/documentation/installation/installing-images/README.md
   https://www.raspberrypi.org/documentation/installation/installing-images/mac.md
   $diskutil list
   $sudo dd bs=1m if=os_image.img of=/dev/flash_disk_device
   or, to show progress:
   $dd if=os_image.img | pv | sudo dd bs=1m of=/dev/flash_disk_device
   If getting "Resource busy", unmount all partitions from the flash card and try again.
   DiskUtility can be used for this. Note: Unmount without Ejecting the device.
 - Boot up the rPi
 - Login with default credentials. (on rPi)
   user: pi
   pass: raspberry
 - Update the system (on rPi)
   $sudo apt-get update
   $sudo apt-get upgrade
 - Enable ssh server via raspi-config (under Advanced options)
   $sudo raspi-config
 - Note to self: Don't forget to install Midnight Commander, otherwise you'll be annoyed with things...
   $sudo apt-get install mc 


Remote connection
=================

 - Ensure that SSH server is enabled on the rPi (see above)
 - Verify that the rPi is visible in your network. (on your machine)
   $ping raspberrypi.local
 - Connect to the rPi. (on your machine)
   $ssh pi@raspberrypi.local


Install Unicorn Hat library
===========================
The following should be done on rPi via SSH or directly.

 - references: 
   http://forums.pimoroni.com/t/raspberry-pi-2-what-works-and-what-doesnt/352
   https://github.com/pimoroni/unicorn-hat
 - Verify that python-dev is installed (may be required by UnicornHat library. ie. compilation will fail without it.)
   $dpkg -s python-dev
   Install it, if it is missing
   $sudo apt-get install python-dev
 - Install python package manager 
   $sudo apt-get install python-pip
 - Verify that PIP was installed
   $pip search unicornhat
 - Install Unicorn Hat library
   $sudo pip install unicornhat


Test the Hat
============

 - Git...
   $sudo apt-get install git
 - Source code with demos. (on rPi)
   $cd ~
   $git clone https://github.com/pimoroni/unicorn-hat.git
 - Test it!
   $cd ~/unicorn-hat/python/examples
   $sudo python rainbow.py


TODO
====
 - read: http://sandyjmacdonald.github.io/2014/12/29/controlling-the-pimoroni-unicorn-hat-with-the-skywriter/