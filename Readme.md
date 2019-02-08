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

[To do]

It's easiest to have a virtual environment up and running, with all these thing in it.

### Data Requirements

[To do]

### Run it

To run the program, simply run `main.py`.

Possible running arguments:
* \[none]
* test
* force

Without any arguments, it wil do a __normal run__. This means it means it checks if a list of system numbers to work with, already exists. If not, it will create one, by loading the list of all BEBB system numbers and then ruling out the system numbers that are already in use in the productive wiki (by checking the dump files in `data/input/xml/*.xml`); if the list is already cached, it simply loads the existing list.  
Then it checks for each system number to do, if the binary marc data is already cached; if not, it wil load this data from `aleph.unibas.ch`, and cache it.  
Finally, it will check, which XML files are already found in the output; those, it will skip, for the others, it will create a new XML file (according to BEBB naming standards) in `data/output/xml` that is an empty letter transcription, but with all necessary meta data from the catalogue.

With the argument `test`, it does a __test run__, that doesn't deliver much of a result, but on the other hand, should run fairly quickly (meaning just a couple of seconds, not several minutes). This is mostly for testing the functionality of the program.  
It does mostly the same as the normal run, but just for a very limited number of system numbers.  
_At some point it would be cool to be able to give an extra argument, how many random system numbers should be run; or extra arguments for specific system numbers to check._  
Other than the normal run, the test run will not skip cached files, but overwrite them.

With the argument `force`, it does a __force everything__ run.  
This does basically the same as the normal run, but it will simply ignore all cached files. So this should be identical to a normal run, there all cached data has been deleted beforehand.


