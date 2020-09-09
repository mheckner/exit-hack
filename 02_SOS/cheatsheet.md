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
