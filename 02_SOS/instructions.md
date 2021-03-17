# Achtung: Lesen Sie erst diese Seite vollständig durch, bevor Sie mit der Aufgabe beginnen.
Diese Aufgabe werden Sie mit der Entwicklungsumgebung Arduino lösen.
Folgen Sie der Anleitung aus der EInladungsemail, um diese zu installieren.

# Arduino IDE starten und das erste Programm auf den Arduino laden
1. Starten Sie die Arduino Entwicklungsumgebung
2. Klicken Sie in das Menü oben in der Arduino Entwicklungsumgebung. Öffnen Sie ein erstes Arduino Beispiel durch Klick auf `Datei->Beispiele->01. Basics->Blink`.
3. Verbinden Sie den Arduino per USB-Kabel mit dem PC
4. Übertragen Sie jetzt das Blink-Beispiel auf den Arduino durch Klick den Button "Hochladen in der Arduino IDE". Die orange LED auf dem Arduino sollte blinken. Möglicherweise wird dieses Programm bereits auf dem neuen Arduino ausgeführt. Verändern Sie die Werte für `delay` (Zeit in Millisekunden) und übertragen Sie das Programm erneut, um zu überprüfen, ob der Upload funktioniert.

**Tipp:** Achten Sie darau, dass Sie im Menü unter `Tools->Port` den Arduino ausgewählt haben. Sonst kann das Programm nicht auf den Arduino übertragen werden.

**Machen Sie erst weiter, wenn die LED blinkt.**

# Bearbeitung der Aufgabe
Für diese Aufgabe existiert eine Datei, die bereits den vollständigen Code enthält, um eine LED leuchten zu lassen, wenn der Benutzer einen Taster auf dem Breadboard drückt.

1. Kopieren Sie diesen Code in die Arduino IDE (und ersetzen den bestehenden Beispielcode). Sie können den Code hier herauskopieren: https://github.com/mheckner/exit-hack/blob/master/02_SOS/solution/sos/sos.ino

Das Ergebnis sollte in etwa so aussehen:

![](../img/arduino.png?raw=true)

2. Übertragen Sie das Programm auf den Arduino durch Klick auf den Button *Hochladen* in der Arduino IDE.

Stecken jetzt den Arduino wieder an. Die LED sollte leuchten, wenn Sie die Taste drücken.

**Passen Sie jetzt den Code der geöffneten Datei so an, dass das SOS Signal bei Tastendruck gesendet wird!**

## Tipps
* [Grundlagen Morsecode](https://github.com/mheckner/exit-hack/blob/master/02_SOS/morsecode.md)
* [Foliensatz zu Arduino](https://github.com/mheckner/exit-hack/tree/master/02_SOS/slides)
* [Cheatsheet mit Codebeispielen und Erklärungen](https://github.com/mheckner/exit-hack/blob/master/02_SOS/cheatsheet_arduino.md)
* Weitere Code- und Verkabelungsbeispiele finden Sie im Ordner [examples](https://github.com/mheckner/exit-hack/tree/master/02_SOS/examples)
* Leider sind nicht alle Widerstände farbig identisch codiert - Sie benötigen einen **220 Ohm** Widerstand für die LED und einen **10 kOhm** für den Button

