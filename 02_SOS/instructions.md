# Virtuelle Maschine starten
Ab jetzt werden Sie auf einem virtuellen Computer arbeiten, d.h. ein Computer, der in Ihrem Computer gestartet wird. Führen Sie zunächst die folgenden Schritte aus:

1. Öffnen Sie dazu das Programm "Virtual Box", das Sie sich im Vorfeld heruntergeladen haben.
2. Starten Sie von dort die virtuelle Maschine "Exit Hack". Ab jetzt arbeiten Sie mit diesem Computer. Warten Sie bis der Computer gestartet ist (dies kann einen Moment dauern).
3. Loggen Sie sich ein, das Passwort lautet "hack", der User ist bereits voreingestellt.

# Arduino IDE starten und das erste Programm auf den Arduino laden
1. Starten Sie die Arduino Entwicklungsumgebung durch Klick auf das Arduino Logo in der linken Seitenleiste (Unendlichkeitssymbol auf grünem Hintergrund).
2. Klicken Sie in das Menü oben in der Arduino Entwicklungsumgebung. Öffnen Sie ein erstes Arduino Beispiel durch Klick auf `Datei->Beispiele->01. Basics->Blink`.
3. Verbinden Sie den Arduino per USB-Kabel mit dem PC
4. Das Linux Betriebssystem Ihres *Computers im Computer* benötigt Zugriff auf den USB-Port. Das folgende Bild zeigt,den dafür notwendigen Klick:
![setup usb in virtual machine](../img/setup_arduino_usb.png?raw=true)
5. Übertragen Sie jetzt das Blink-Beispiel auf den Arduino durch Klick den Button "Hochladen in der Arduino IDE". Eine LED auf dem Arduino sollte blinken.

**Machen Sie erst weiter, wenn die LED blinkt.**

# Bearbeitung der Aufgabe
Öffnen Sie den Ordner `exit-hack` auf dem Desktop und navigieren zum Ordner `02_SOS/solution/sos`.
Dort finden Sie die Datei `sos.ino`. Diese enthält bereits den vollständigen Code, um eine LED leuchten zu lassen, wenn der Benutzer einen Taster auf dem Breadboard drückt.
**Öffnen Sie aus der Arduino IDE heraus die Datei sos.ino (Die Datei finden Sie auf dem Schreibtisch).**

Beginnen Sie damit die folgende Verkabelung herzustellen:
![wiring button led](./examples/hello_world_blynk_button/hello_world_blynk_button.png?raw=true)

Übertragen Sie das Programm auf den Arduino durch Klick auf den Button "Hochladen in der Arduino IDE". Die LED sollte leuchten, wenn Sie die Taste drücken.

**Senden Sie jetzt das SOS Signal bei Tastendruck!**

## Tipps
* [Grundlagen Morsecode](https://github.com/mheckner/exit-hack/blob/master/02_SOS/morsecode.md)
* [Foliensatz zu Arduino](https://github.com/mheckner/exit-hack/tree/master/02_SOS/slides)
* [Cheatsheet mit Codebeispielen und Erklärungen](https://github.com/mheckner/exit-hack/blob/master/02_SOS/cheatsheet_arduino.md)
* Weitere Code- und Verkabelungsbeispiele finden Sie im Ordner [examples](https://github.com/mheckner/exit-hack/tree/master/02_SOS/examples)
* Leider sind nicht alle Widerstände farbig identisch codiert - Sie benötigen einen **220 Ohm** Widerstand

