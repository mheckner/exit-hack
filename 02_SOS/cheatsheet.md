# Cheatsheet for SOS

## Arduino starter file
The following code contains a minimal, working Arduino starter file.
```c
 void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
```

## Additional setup
Your Arduino IDE needs access to the Arduino over USB. Follow these steps, before trying to upload a program to the Arduino:

### Connect Arduino through USB
First plug the Arduino into one of the USB ports of your computer.

### Give virtual machine access to the Arduino over USB
The Linux system inside the virtual machine needs to get access to the plugged USB device. The following picture shows where to click:
![setup usb in virtual machine](../img/setup_arduino_usb.png?raw=true)

## Resistors
You need a 220 Ohm resistor for this task.


## Basic control structures in programming

### Comments
Comments are intended as descriptions for the developer (i.e. the writer of the code) and will be ignored by the computer. Comments can be added like this anywhere in the file:
```c
 // Hello, I am a comment
```

### Functions
A function contains a set of commands that the computer can execute. The following code does XYZ:

```c
void setup() {
  // put your setup code here, to run once:

}
```

### Loops
A loop is written as follows, where N represents the number of times the code between the curly braces is repeated.

```c
for (int i=0; i++; i<N) {
  // repeat this
}
```


### Conditional statements
The else block can be omitted.

```c
if (condition is true) {
  //execute this
} else {
  // execute this
}
```
