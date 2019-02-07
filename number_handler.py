force_all = False
is_test = False

def get_used_sys_nos(force, test):
    print("Getting System Numbers in Use...")
    print("Is Force Run: {}".format(force))
    force_all = force
    print("Is Test Run: {}".format(test))
    is_test = test

    all_numbers = get_all_sys_nos()
    """Do Stuff here"""

    print("Done getting Sys. Numbers.\n")
    return


def get_all_sys_nos():
    print("loading numbers...")
    res = []
    with open("data/input/all_numbers.txt") as f:
        res = f.readlines()
    print("found numbers: " + str(len(res)))
    print(res)
    return res

