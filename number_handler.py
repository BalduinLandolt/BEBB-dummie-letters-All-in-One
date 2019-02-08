import os
from lxml import etree
import random


force_all = False
is_test = False


def get_sys_nos_to_work_with(force, test):
    print("Getting System Numbers in Use...")
    print("Is Force Run: {}".format(force))
    global force_all
    force_all = force
    print("Is Test Run: {}".format(test))
    global is_test
    is_test = test

    all_numbers = get_all_sys_nos()
    used_numbers = get_used_sys_no_list()
    list_for_dummies = get_list_of_numbers_to_work_with(all_numbers, used_numbers)

    print("Got a List to work with: {}".format(list_for_dummies))

    # TODO Do Stuff here

    print("Done getting Sys. Numbers.\n")
    return list_for_dummies


def get_all_sys_nos():
    print("loading 'all numbers'...")
    with open("data/input/all_numbers.txt") as f:
        res = f.readlines()
    print("found numbers: " + str(len(res)))
    print(res)
    return res


def get_used_sys_no_list():
    print("loading 'used numbers'...")

    if force_all or is_test:
        print("force or test run.")
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
        # print(f)
        sys_no = get_by_name(f)
        res.append(sys_no)

    print("Result: ")
    print(res)
    return res


def get_by_name(name):
    # print("trying to load data by name: "+name)
    prefix = "data/input/xml/"
    res = ""
    try:
        root = etree.parse(prefix + name, etree.XMLParser(load_dtd=True)).getroot()
        # print(etree.tostring(root))
        res = root.get("catalogue_id")
        # print(res)
        # print("got file by name.\n")
        # print("Got System Number: {}".format(res))
    except OSError:
        print("Could not read File: " + name + "\n")
    return res


def read_used_nos():
    print("Reading used System Numbers from File...")
    with open("data/tmp/existing_numbers.txt", "r") as f:
        res = f.readlines()
    return res


def write_used_nos(used_nos):
    print("Writing used System Numbers to File...")
    with open("data/tmp/existing_numbers.txt", "w") as f:
        for l in used_nos:
            f.write(l + "\n")

    # TODO does that turn out utf-8?


def get_list_of_numbers_to_work_with(all_nos, used):
    res = []
    for no in all_nos:
        if no not in used:
            res.append(no)

    if is_test:
        test_res = []
        for i in range(5):
            test_res.append(res[random.randint(0, len(res))])
        print("For test purposes, list has been shortened from {} to {}.".format(len(res), len(test_res)))
        return test_res

    return res
