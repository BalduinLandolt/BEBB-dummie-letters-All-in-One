import os
from lxml import etree
import random



def get_used_sys_nos(force, test):
    print("Getting System Numbers in Use...")
    print("Is Force Run: {}".format(force))
    global force_all
    force_all = force
    print("Is Test Run: {}".format(test))
    global is_test
    is_test = test

    all_numbers = get_all_sys_nos()
    used_numbers = get_used_sys_no_list()
    """Do Stuff here"""

    print("Done getting Sys. Numbers.\n")
    return


def get_all_sys_nos():
    print("loading 'all numbers'...")
    res = []
    with open("data/input/all_numbers.txt") as f:
        res = f.readlines()
    print("found numbers: " + str(len(res)))
    print(res)
    return res


def get_used_sys_no_list():
    print("loading 'used numbers'...")

    used_nos = []

    if force_all:
        used_nos = grab_used_nos()
        write_used_nos(used_nos)
    else:
        if os.path.isfile("./data/tmp/existing_numbers.txt"):
            print("File 'existing_numbers.txt' already exists. Loading list from cache instead.")
            used_nos = read_used_nos()
        else:
            used_nos = grab_used_nos()
            write_used_nos(used_nos)

    print("Got Already Used System Numbers now.")
    print(used_nos)

    return used_nos


def grab_used_nos():
    # TODO implement this

    files = os.listdir("data/input/xml")
    print("found:")
    print(files)

    if is_test:
        tmp = []
        for i in range(5):
            tmp.append(files.pop(random.randint(0,len(files))))
        files = tmp
        print("Reduced List for test purposes: {}".format(files))

    print("")
    res = []
    for file in files:
        print(file)
        sys_no = get_by_name(file)
        res.append(sys_no)

    print("Result: ")
    print(res)
    """with open("input/existing_numbers.txt", "w") as out_file:
        print(res, file=out_file)

    print("handled all files in folder.")"""

    return res


def get_by_name(name):
    print("trying to load data by name ("+name+")...")
    prefix = "data/input/xml/"
    sysNo = ""
    try:
        root = etree.parse(prefix + name, etree.XMLParser(load_dtd=True)).getroot()
        print(etree.tostring(root))
        sysNo = root.get("catalogue_id")
        print(sysNo)
        print("got file by name.\n")
    except OSError:
        print("Could not read File: " + name + "\n")
    return sysNo


def read_used_nos():
    # TODO implement this

    """

    """
    res = []
    return res


def write_used_nos(list):
    # TODO implement this

    """

    """
