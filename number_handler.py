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

    # TODO Do Stuff here

    print("Done getting Sys. Numbers.\n")
    return


def get_all_sys_nos():
    print("loading 'all numbers'...")
    with open("data/input/all_numbers.txt") as f:
        res = f.readlines()
    print("found numbers: " + str(len(res)))
    print(res)
    return res


def get_used_sys_no_list():
    print("loading 'used numbers'...")

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
    files = os.listdir("data/input/xml")
    print("found {} files: {}".format(len(files), files))

    if is_test:
        tmp = []
        for i in range(5):
            tmp.append(files.pop(random.randint(0, len(files))))
        files = tmp
        print("Reduced List for test purposes to {} files: {}".format(len(files), files))

    print("")
    res = []
    for f in files:
        print(f)
        sys_no = get_by_name(f)
        res.append(sys_no)

    print("Result: ")
    print(res)
    return res


def get_by_name(name):
    print("trying to load data by name ("+name+")...")
    prefix = "data/input/xml/"
    res = ""
    try:
        root = etree.parse(prefix + name, etree.XMLParser(load_dtd=True)).getroot()
        print(etree.tostring(root))
        res = root.get("catalogue_id")
        print(res)
        print("got file by name.\n")
    except OSError:
        print("Could not read File: " + name + "\n")
    return res


def read_used_nos():
    # TODO implement this

    """

    """
    res = []
    return res


def write_used_nos(used_nos):
    # TODO implement this

    """

    """
    """
    with open("input/existing_numbers.txt", "w") as out_file:
        print(res, file=out_file)
    """

