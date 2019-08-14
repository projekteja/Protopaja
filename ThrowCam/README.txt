!!!
To make sure you have all the proper python addons make sure to 
read INSTALLME.txt for the correct pip commands to setup python properly
!!!

Prepare the device:

1. Make sure your batteries have power : you can charge them with plugging a micro-USB charger to the powersupply circuit
while the battery is attached and the circuit is detached from the main device

2. Power on the device : power switch attached to the powersupply will turn on the device

3. Let the device boot : booting will take 10 - 20 seconds

Prepare the software:

1. After device prep, connect your computer to wifi with settings written in SETTINGS.txt

2. Start your ThrowCam-software : to start the software either press the ThrowCam-shortcut or start ThrowCam.pyw

3. Make sure everything is correct : at this point you should see 3 video feeds from the device in the UI-program window and
hear audio from the device, if not power off the divice and check all connections and prep the device again

4. Connect SSH :  to gain access to LEDs and angle sensing functions first make sure you have pressed "CONNECT SSH", this
will try connect your computer to the device with SSH and if successful connection indicator next to the button will turn
green

5. Connect AUS : to send your own microphone feed to the device, you have to make sure have pressed the "CONNECT AUS" - button
but DO NOT PRESS THIS BUTTON BEFORE PRESSING CONNECT SSH - BUTTON, THIS WILL CRASH THE PROGRAM, if the AUS (Audio upstream) was
setup successfully the connection indicator will turn green

