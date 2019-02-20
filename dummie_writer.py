import os
import marc_handler as mc
import codecs

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

    xml_string = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    xml_string = xml_string + "<letter xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n"
    xml_string = xml_string + "        xsi:noNamespaceSchemaLocation=\"../Schema_and_DTD/letter.xsd\"\n"
    xml_string = xml_string + "        title=\"{}\"\n".format(name)
    xml_string = xml_string + "        catalogue_id=\"{}\"".format(mc.get_system_number(data_set)) # TODO continue


    write_to_file(path, xml_string)
    return


def write_to_file(path, data):
    if is_test:
        print("Writing to File...\nData:\n{}".format(data))

    with codecs.open(path, "w", "utf-8") as f:
        f.write(data)

    print("Done Writing file.")
    return


def generate_name(data_set):
    # TODO handle unknown recipients
    # TODO namen encoding stimmt nicht immer: c-cedie und so

    date = mc.get_date(data_set)
    if date is None:
        date = "0000-00-00"
    date = date.replace(".", "-")

    authors = mc.get_author(data_set)
    author = authors[0]
    author_name = author['name']
    author_name = author_name.replace(" ", "_")
    author_name = author_name.replace("'", "")
    author_name = author_name.replace(",", "")

    recipients = mc.get_recipient(data_set)
    recipient = recipients[0]
    rec_name = recipient['name']
    rec_name = rec_name.replace(" ", "_")
    rec_name = rec_name.replace("'", "")
    rec_name = rec_name.replace(",", "")

    res = date + "_" + author_name + "-" + rec_name
    return res
