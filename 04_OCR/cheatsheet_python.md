# Cheatsheet for Python

## Python "Hello World!"
The following code contains a minimal, working Python file (hello_world.py).
```python
def main():
    print("Hello world!")

if __name__ == "__main__":
    main()
```

To run this file, type the following command:
```shell
python3 hello_world.py
```


## Basic control structures in Python

### Comments
Comments are intended as descriptions for the developer (i.e. the writer of the code) and will be ignored by the computer. Comments can be added like this anywhere in the file:
```python
 #Hello, I am a comment
```

### Functions
A function contains a set of commands that the computer can execute. The following code does XYZ:

```python
def printHello():
    print("Hello")
```
### Functions with parameters
A function can also receive information. For this purpose a variable is added between the round brackets of the function definition. In the following example msg has the value
"Hello World!"

```python
def main():
    message = "Hello World!"
    printMessage(message)

def printMessage(msg):
    print(msg)
```
