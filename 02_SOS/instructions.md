Ab jetzt werden Sie auf einem virtuellen Computer arbeiten, d.h. ein Computer, der in Ihrem Computer gestartet wird.

Öffnen Sie dazu das Programm "Virtual Box", das Sie sich im Vorfeld heruntergeladen haben.

Starten Sie von dort die virtuelle Maschine "Exit Hack".
Ab jetzt arbeiten Sie mit diesem Computer.

Warten Sie bis der Computer gestartet ist (dies kann einen Moment dauern).

Loggen Sie sich ein, das Passwort lautet "hack", der User ist bereits voreingestellt.

Öffnen Sie den Ordner Exit-Hack auf dem Desktop und navigieren zum Ordner 02_SOS/solution/sos.
Dort finden Sie die Datei sos.ino

Starten Sie die Arduino Entwicklungsumgebung durch Klick auf das Arduino Logo in der linken Seitenleiste.
Öffnen Sie von dort aus die Datei sos.ino (Die Datei finden Sie auf dem Schreibtisch).

Beginnen Sie damit die Verkabelung herzustellen (vgl. dazu LINK).
Die Datei sos.ino enthält bereits einen funktionierenden Beispielcode.

Schließen Sie den Arduino an:

## Additional setup
Your Arduino IDE needs access to the Arduino over USB. Follow these steps, before trying to upload a program to the Arduino:

### Connect Arduino through USB
First plug the Arduino into one of the USB ports of your computer.

### Give virtual machine access to the Arduino over USB
The Linux system inside the virtual machine needs to get access to the plugged USB device. The following picture shows where to click:
![setup usb in virtual machine](../img/setup_arduino_usb.png?raw=true)

## Resistors
You need a 220 Ohm resistor for this task.

Übertragen Sie das Programm auf den Arduino durch Klick auf den Button "Hochladen in der Arduino IDE". Die LED sollte leuchten, wenn Sie die Taste drücken.

Weitere Tipps finden Sie im Ordner examples und hier LINK
