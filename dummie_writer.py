import os, marc_handler

force_all = False
is_test = False
marc_data_list = []


def write_dummies(data_list, force, test):
    print("Writing Dummie XML Files to Output...")
    print("Is Force Run: {}".format(force))
    global force_all
    force_all = force
    print("Is Test Run: {}".format(test))
    global is_test
    is_test = test
    print("Sets of Data: {}".format(len(data_list)))
    global marc_data_list
    marc_data_list = data_list

    if is_test:
        try_to_write_dummy(marc_data_list[0])
    else:
        for d in marc_data_list:
            try_to_write_dummy(d)

    print("Done writing Dummies.\n")


def try_to_write_dummy(data_set):
    name = generate_name(data_set)
    if not force_all:
        if os.path.isfile("data/output/xml/" + name + ".xml"):
            print("File already exists: {}".format(name))
            return
    write_dummy(name, data_set)


def write_dummy(name, data_set):
    # TODO implement
    return


def generate_name(data_set):
    # TODO implement
    return ""
