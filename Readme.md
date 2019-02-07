# XML-Dummie generator for BEBB

##### (balduin.landolt@unibas.ch)

This Program creates empty XML files for letters that are relevant to the BEBB project, but do not existe in the productive Wiki as of yet.

## How to work it:

Make sure all requirements are met and follow the instruction.

### Running Requirements

It only runs on Python 2.7. (Tested on Python 2.7.15.)
To ensure functionality I recommend using the same.

Required Python Modules:
* lxml
* pymarc
* ply
* PyZ3950

The first three can be installed via pip. (Use Pycharm Modules or type in the console \[with admin rights] `pip install lxml` or the other modules respectively.)

PyZ3950 is a bit annoying...

[more comming soon...]

It's easiest to have a virtual environment up and running, with all these thing in it.

### Run it

To run the program, simply run `main.py`.

Possible running arguments:
* \[none]
* test
* force

Without any arguments, it wil do a normal run: 

[explain]

