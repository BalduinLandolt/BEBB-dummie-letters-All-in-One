"""
This Script contains all functions for handling the determination of that system numbers to work with

This script provides a number of functions to handle BEBB system numbers.
The main notion is to read the list `all_numbers.txt` and to
extract the system numbers already in use from the XML-files in `data/input/xml`.
All numbers found in the .txt but not found in any .xml needs to be processed further,
and eventually have a dummy XML file created.
"""

import os
from lxml import etree
import random
import sys


force_all = False
is_test = False
testable = None


def get_sys_nos_to_work_with(force, test, testable_no):
    """
    Get a list of system numbers to work with in further steps.

    This umbrella function is meant to be called from another script
    - presumably `main.py` - to retrieve a list of system numbers, for which
    dummy letters are to be created.
    The actual process of selection is left to the functions called here in;
    but the core concept is: To get an amount `all numbers` aswell as
    an amount `numbers in use`, and then to subtract the latter from the fist;
    this leaves the amount `numbers not yet in use` that is returned.

    :param force: if true, it is executed as a force run.
    (Everything is done anew; things already done are overwritten.)
    :param test: If true, it is a test run.
    (Either a small random sample of numbers is processed or only one given number is processed
    - depending on testable_no.)
    :param testable_no: In case of a test run, if this is None, the test run is executed with random system numbers;
    if this is a valid system number, the test run will be executed on the letter specified by the system number.
    :return: Returns a list of system numbers that occur in `all_numbers.txt` but not in the XML files.
    """

    print("Getting System Numbers in Use...")
    print("Is Force Run: {}".format(force))
    global force_all
    force_all = force
    print("Is Test Run: {}".format(test))
    global is_test
    is_test = test
    global testable
    testable = testable_no

    all_numbers = get_all_sys_nos()
    used_numbers = get_used_sys_no_list()
    list_for_dummies = get_list_of_numbers_to_work_with(all_numbers, used_numbers)

    print("Got a List to work with: {}".format(list_for_dummies))

    print("Done getting Sys. Numbers.\n")
    return list_for_dummies


def crop_list(lst):
    """
    strips all strings in a list.

    Iterates over a list of strings and performs strip() on each one.
    :param lst: the list of string with potential heading/tailing whitespaces
    :return: a list with the cropped strings
    """

    out = []
    for l in lst:
        out.append(l.strip())
    return out


def get_all_sys_nos():
    """
    reads all system numbers from the file `data/input/all_numbers.txt`

    :return: a list with all system numbers relevant for BEBB
    """

    print("loading 'all numbers'...")
    with open("data/input/all_numbers.txt") as f:
        res = f.readlines()
    print("found numbers: " + str(len(res)))
    res = crop_list(res)
#    print(res)
    return res


def get_used_sys_no_list():
    """
    gets a list of the system numbers already in use.

    This function returns a list of system numbers already in use.
    In case of a normal run, if such a list is already cached, it simply returns this list (without checking it),
    in case of a force or test run, or if none exists in cache, a new list is generated.
    Generating this list is based on the XML files in `data/input/xml`, so unless all files
    that exist in BEBB at a given time, are actually in said folder, this list has no way of being exhaustive.
    :return: a list of the system numbers already in use
    """

    print("loading 'used numbers'...")

    if force_all or is_test:
        print("force or test run.")
        used_nos = grab_used_nos()
        __write_used_nos(used_nos)
    else:
        if os.path.isfile("./data/tmp/existing_numbers.txt"):
            print("File 'existing_numbers.txt' already exists. Loading list from cache instead.")
            used_nos = __read_used_nos()
        else:
            used_nos = grab_used_nos()
            __write_used_nos(used_nos)

    used_nos = crop_list(used_nos)
    print("Got Already Used System Numbers now.\n")
#    print(used_nos)

    return used_nos


def grab_used_nos():
    """
    This method grabs the used system numbers from the file system.

    This method is called by get_used_sys_no_list() under certain logical conditions.
    It doesn't do the actual reading of the XML files, but looks for files
    and calls get_by_name() for each of them.
    :return: Returns a list of system numbers for each XML file found.
    """

    files = os.listdir("data/input/xml")
    print("found {} files.".format(len(files)))
    #print("files: {}".format(files))

    print("\nloading system numbers from files...\n")
    res = []
    i = 1
    max = len(files)+1
    for f in files:
        sys.stdout.write("\r{} of {}".format(i, max))
        sys.stdout.flush()
        i = i + 1
        # print(f)
        sys_no = get_by_name(f)
        res.append(sys_no)

    print("\ngot {} numbers to work with.".format(len(res)))
#    print("Result: ")
#    print(res)
    return res


def get_by_name(name):
    """
    Gets system Numbers from XMLs by file name.

    :param name: file name of the xml file.
    :return: system number of the xml file.
    """

    prefix = "data/input/xml/"
    res = ""
    try:
        root = etree.parse(prefix + name, etree.XMLParser(load_dtd=True)).getroot()
        res = root.get("catalogue_id")
    except OSError:
        print("Could not read File: " + name + "\n")
    return res


def __read_used_nos():
    print("Reading used System Numbers from File...")
    with open("data/tmp/existing_numbers.txt", "r") as f:
        res = f.readlines()
    return res


def __write_used_nos(used_nos):
    print("Writing used System Numbers to File...")
    with open("data/tmp/existing_numbers.txt", "w") as f:
        for l in used_nos:
            f.write(l + "\n")


def get_list_of_numbers_to_work_with(all_nos, used):
    """
    creates a list of all numbers contained in the all- list but not in the used-list

    :param all_nos: list of all relevant system numbers
    :param used: list of all system numbers already used in the project
    :return: a list containing all numbers in `all_nos` but not in `used`.
    """

    res = []
    for no in all_nos:
        if no not in used:
            res.append(no)

    if is_test:
        test_res = []
        if testable is None:
            for i in range(5):
                test_res.append(res[random.randint(0, len(res)-1)])
            print("For test purposes, list has been shortened from {} to {}.".format(len(res), len(test_res)))
            return test_res
        else:
            test_res.append(testable)
            return test_res

    res = crop_list(res)
    return res
