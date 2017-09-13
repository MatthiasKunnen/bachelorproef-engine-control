# Engine control
This project allows you to control an engine using a Raspberry Pi. I have
used this in combination with a 
[L298N module](http://www.instructables.com/id/Control-DC-and-stepper-motors-with-L298N-Dual-Moto/)
to control a Lego engine. This project was made as a demo for my 
[thesis](https://github.com/MatthiasKunnen/bachelorproef).
 
# Setup 
There is a Lego door on a rail that is controlled by a Lego engine. This 
engine is connected to the L289N module, which is connected to the GPIO header
of the Raspberry Pi. The Raspberry is on the same network as a computer which
acts as the server.

Upon insertion of a USB device in the Raspberry Pi, the `access_listener`
script will mount the partition(s) on the device and check if `nonce` and
`nonce.sig` are present. These files will be sent to the server to check if
access should be granted. The server will respond and let the Raspberry Pi
know whether it should keep the door shut or turn on the engine thereby
opening the door. The door will automatically close.

The project contains several scripts that can be used to configure, calibrate
and test the engine.

Edit `default_engine_control.py` to give in the GPIO pins that control the
engine.

Run `power_state_test.py` to test the power states. 

Use `measure_engine_time.py` to detect how long the engine should run in
order to open the door. 

Run `open_and_close.py` to open and close the door. Use the `-h` flag to show
all available options.

The main script that will actively listen for newly inserted partitions, poll
the server and interact with the user of the access control system is the
`access_listener.py`. Use the `-h` flag to show
all available options.
