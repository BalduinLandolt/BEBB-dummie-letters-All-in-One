import os

force_all = False
is_test = False

def get_used_sys_nos(force, test):
    print("Getting System Numbers in Use...")
    print("Is Force Run: {}".format(force))
    force_all = force
    print("Is Test Run: {}".format(test))
    is_test = test

    all_numbers = get_all_sys_nos()
    used_numbers = get_used_sys_nos()
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


def get_used_sys_nos():
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
    """
    print("getting a list of the contents of the directory...")
    files = listdir("input/xml")
    print("found:")
    print(files)
    print()
    res = ""
    for file in files:
        print(file)
        sys_no = get_by_name(len(file))
        res += sys_no + "\n"

    print("Result: ")
    print(res)
    with open("input/existing_numbers.txt", "w") as out_file:
        print(res, file=out_file)

    print("handled all files in folder.")
    """


def read_used_nos():
    """

    """


def write_used_nos():
    """

    """
