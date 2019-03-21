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

PyZ3950 is a bit harder to install:  
(see https://github.com/asl2/PyZ3950 and http://www.panix.com/~asl2/software/PyZ3950/)  
Clone git repository (https://github.com/asl2/PyZ3950) and run `setup.py install` with admin rights (e.g. `sudo python setup.py install` under mac or under windows cmd.exe with admin rights respectively).  
Make sure you're the python installation, where you want the Z39.50 module to be located; so, if you're using a virtual environment, just typing `python` will not run that. In this case you'll have to specify the path to the python installation (e.g. `C:\path\to\virtual\environment\python.exe setup.py install`).

It's easiest to have a virtual environment up and running, with all these thing in it.

### Data Requirements

In order to work correctly, the program requires particular set of input data in the correct location. Make sure this is the case before trying to run the program.

When cloning the program from Github, most of the folder structure should already be given: In the same folder as the `.py` files, there needs to be a folder `data`; in there again, a folder `input` is required; that again should contain `Schema_and_DTD` with the schema to validate the `.xml`files in it.

In `data/input` there ought to be a file `all_numbers.txt`, which is __absolutely crucial__, but should be provided by the Github clone. It's a plain text file containing all system numbers of letters relevant to the BEBB Project in the format `000054744`, each number on a new line. (Should be 5423 lines.)

Another folder, `data/input/xml` is not provided by the clone, so __you need to add this folder `xml` in `data/input` manually!__

__In this folder, you need to copy all `.xml` files of all the letters, to wich there are `.xml` files (i.e. from the productive wiki, the non-productive wiki and any future editorial activity).__ No other files should be in this folder. (By March 2019, there were 3213 files; it can by no means be fewer than this at any time in the future.)

### Run it

To run the program, simply run `main.py`.

Possible running arguments:
* \[none]
* test
* test \[System Number]
* force

Without any arguments, it wil do a __normal run__. This means it means it checks if a list of system numbers to work with, already exists. If not, it will create one, by loading the list of all BEBB system numbers and then ruling out the system numbers that are already in use in the productive wiki (by checking the dump files in `data/input/xml/*.xml`); if the list is already cached, it simply loads the existing list.  
Then it checks for each system number to do, if the binary marc data is already cached; if not, it wil load this data from `aleph.unibas.ch`, and cache it.  
Finally, it will check, which XML files are already found in the output; those, it will skip, for the others, it will create a new XML file (according to BEBB naming standards) in `data/output/xml` that is an empty letter transcription, but with all necessary meta data from the catalogue.

With the argument `test`, it does a __test run__, that doesn't deliver much of a result, but on the other hand, should run fairly quickly (meaning just a couple of seconds, not several minutes). This is mostly for testing the functionality of the program.  
It does mostly the same as the normal run, but just for a very limited number of system numbers.  
_Running `test [System Number]`(e.g. `test 000054744`) will force the program to test for the letter with this specific system number. This can be handy to test certain problematic cases, without leafing it to chance, if the test run encounters a letter that can cause this problem._  
Other than the normal run, the test run will not skip cached files, but overwrite them.

With the argument `force`, it does a __force everything__ run.  
This does basically the same as the normal run, but it will simply ignore all cached files. So this should be identical to a normal run, there all cached data has been deleted beforehand.
