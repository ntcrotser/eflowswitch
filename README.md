
eFlowswitch is an application intended to combine the Raspberry Pi SBC, a Hall Effect Sensor based flow meter, and chemical dosing pumps which make use of dry circut based flowswitches.

I'll be giving a whole lot of information and tips over the course of making this application, so don't be bogus.

TODO:
Impliment pulse counting to record total volume of water measured by meter.
Impliment override to activate pump on demand.



LICENSE:
All of the files in this project are licensed under the MIT (1987) license.  A copy of the
license is available in the LICENSE.txt file.

--------------------RASPBERRYPI 4 GPIO CHEATSHEET----------------------
|                                                                     |
|                                                                     |
| Sensor Power------3v---------XX  XX----------5v------- Relay Power  |
|                     GPIO02-- 03  04 --5v                            |   
|                     GPIO03-- 05  XX----------GND------ Relay GND    |
|                     GPIO04-- 07  08 --GPIO14                        |      
| Sensor GND--------GND--------XX  10 --GPIO15                        |     
|                     GPIO17-- 11  12 --GPIO18                        |    
|                     GPIO27-- 13  14 --GND                           |  
| Sensor Signal----GPIO22------XX  XX--------GPIO23----- Relay Sensor |
|                         3v-- 17  18 --GPIO24                        |
|                     GPIO10-- 19  20 --GND                           |
|                     GPIO09-- 21  22 --GPIO25                        |
|                     GPIO11-- 23  24 --GPIO08                        |
|                        GND-- 25  26 --GPIO07                        |
|                     GPIO00-- 27  28 --GPIO01                        |
|                     GPIO05-- 29  30 --GND                           |
|                     GPIO06-- 31  32 --GPIO12                        |
|                     GPIO13-- 33  34 --GND                           |
|                     GPIO19-- 35  36 --GPIO16                        |
|                     GPIO26-- 37  38 --GPIO20                        |
|                        GND-- 39  40 --GPIO21                        |
-----------------------------------------------------------------------
