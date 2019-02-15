import os
import marc_handler as mc

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
    print("Sets of Data: {}\n".format(len(data_list)))
    global marc_data_list
    marc_data_list = data_list

    if is_test:
        try_to_write_dummy(marc_data_list[0])
    else:
        for d in marc_data_list:
            try_to_write_dummy(d)

    print("\nDone writing Dummies.\n")


def try_to_write_dummy(data_set):
    name = generate_name(data_set)
    path = "data/output/xml/" + name + ".xml"
    if not force_all:
        if os.path.isfile(path):
            print("File already exists: {}".format(path))
            return
    write_dummy(name, path, data_set)


def write_dummy(name, path, data_set):
    print("Writing file: {}".format(path))

    # TODO implement

    print("Done Writing file.")
    return


def generate_name(data_set):
    date = mc.get_date(data_set)
    date = date.replace(".", "-")

    authors = mc.get_author(data_set)
    author = authors[0]
    author_name = author['name']
    author_name = author_name.replace(" ", "_")
    author_name = author_name.replace("'", "")
    author_name = author_name.replace(",", "")

    # TODO can there be multiple authors? What are naming conventiones in these cases?

    recipients = mc.get_recipient(data_set)
    recipient = recipients[0]
    rec_name = recipient['name']
    rec_name = rec_name.replace(" ", "_")
    rec_name = rec_name.replace("'", "")
    rec_name = rec_name.replace(",", "")

    # TODO dito

    res = date + "_" + author_name + "-" + rec_name
    return res
