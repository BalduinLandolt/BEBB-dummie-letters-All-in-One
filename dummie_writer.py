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
        write_dummy(marc_data_list[0])
    else:
        for d in marc_data_list:
            write_dummy(d)

    print("Done writing Dummies.\n")


def write_dummy(data_set):
    """"""
