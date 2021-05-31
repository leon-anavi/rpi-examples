# rpi-examples

This repository provides various examples for using peripheral devices such as sensors, buzzers, relays and add-on boards on Raspberry Pi single board computers written in popular programming languages C, C++, Python, etc. All examples are available under MIT license.

These examples are appropriate for beginners. Hopefully, they will encourage more developers to join the Raspberry Pi community and to help them get started easily with various peripheral devices for both professional and hobby and DIY projects.

# Videos

* Buzzer: https://www.youtube.com/watch?v=j8HnKM58QXk
* LM75A: https://www.youtube.com/watch?v=pyg27uj0Xns
* HTU21D: https://www.youtube.com/watch?v=A_yruJtYUwE

# Notes

If you are interested in running any of the examples for I2C written in C/C++ as a regular user (not root) perform the following steps:
* Remove line "wiringPiSetup();" in "HTU21D_test.c"
* Add your user in "i2c" group

## Buzzer

### C

#### Beep

Simple application to test if a piezo buzzer attached to pin 11 is working.

Install [wiringPi](http://wiringpi.com/download-and-install/) and after that execute the following command to build the application:

```
cd buzzer/c/
gcc beep.c -o beep -lwiringPi -std=c99
```

Execute the following command to run the application:
```
sudo ./beep
```

#### Star Wars

Implementation of the Imperial March from Star Wars.

Install [wiringPi](http://wiringpi.com/download-and-install/) and after that execute the following command to build the application:

```
cd buzzer/c/
gcc starwars.c -o starwars -lwiringPi -std=c99
```

Execute the following command to play the Imperial March:
```
sudo ./starwars
```

#### TSL2561

Install i2c tools:
```
sudo apt-get install i2c-tools

```

Enable i2c on Raspberry Pi with Raspian GNU/Linux distribution:
```
sudo raspi-config
```

Go to Advanced Options > A7 I2C and reboot the board

Verify that TSL2561 is detected on i2c address 39 on bus 1:
```
pi@raspberrypi:~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```

Build and run the source code
```
cd TSL2561/c/
make
./TSL2561_test
```

## MAX44009 Ambient Light Sensor Module

Build and run the source code
```
cd MAX44009/c/
make
./MAX44009_test
```

The example written in the C programming language has been cotributed by Pixel_K.

## PN532 NFC Module

* Install Adafruit Python PN532:

```
sudo apt-get update
sudo apt-get install build-essential python-dev git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_PN532.git
cd Adafruit_Python_PN532
sudo python setup.py install
```

* Clone rpi-examples:

```
cd ~
git clone https://github.com/leon-anavi/rpi-examples.git
```

* Save data to RFID/NFC card

```
cd ~/rpi-examples/PN532/python
sudo python rfid-save.py
```

* Listen and scan for RFID/NFC cards

```
cd ~/rpi-examples/PN532/python
sudo python rfid-scan.py
```
