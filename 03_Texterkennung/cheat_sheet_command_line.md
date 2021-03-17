# Cheatsheet Command Line
Typically today, users interact with a computer through a graphical user interface and navigate through folders by pointing and clicking with a cursor. In programming however, this is often done through typing commands, instead of clicking. This page explains some typical commands that you might need in order to solve the exit coding game.

Those commands are typed in the shell. The following image shows the state of the shell after the user has typed in the command `pwd`, followed by hitting the enter key. In this case the result of this command (`/home/runner/exit-coding-game`) is shown in the next line.

![typing commands in the repl.it shell](../img/shell.png?raw=true)

**Commands are typed on one line and are executed by hitting the enter key.**

### Running the code in a Python script
To run (or execute) the code in the Python file `hello_world.py`, type the following command:
```shell
python3 hello_world.py
```
For this to work, the Python file must be in the same folder. The following sections explain how to navigate between folders.

### Showing the path to the current folder
Type `pwd` to show the path to the current folder:
```console
~/exit-coding-game$ pwd
/home/runner/exit-coding-game
```
Note that the user is currently in the folder `/exit-coding-game` and `pwd` is the command that the user types (followed by enter). 
`/home/runner/exit-coding-game` is the output (i.e. the answer) of the command `pwd`.

### Changing into a folder one level down (i.e. clicking into a folder)
Type the `cd` (change directory) command followed by space and a folder name to navigate into the folder:
```console
~/exit-coding-game$ cd exit-hack
~/exit-coding-game/exit-hack$ 
```
In the example above, the user changed from the folder `exit-coding-game`into the folder `exit-hack`.

### Changing into a folder one level up (i.e. clicking into the parent folder of the current folder)
Type `cd ..` (again, change directory) to navigate into a folder one level higher:
```console
~/exit-coding-game/exit-hack$ cd ..
~/exit-coding-game$ 
```
In the example above, the user went from the folder `exit-hack` into the folder `exit-coding-game`.

### Showing all files in the current folder
Type `ls`to show all files (and subfolders) within the current folder:
```console
~/.../exit-hack/03_Texterkennung$ ls
cheatsheet_python.md  examples  instructions  slides  solution
```
In this case the folder `03_Texterkennung` contains a file `cheatsheet.md` and the folders `examples`, `instructions`, `slides` and `solutions`. 



