import os
import marc_handler as mc
import codecs
import traceback

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

    try:
        write_dummy(name, path, data_set)
    except Exception as e:
        print("\n\n\n\n!!!!!!!!!!!!!!!!!!!! Error !!!!!!!!!!!!!!!!!!!!!")
        print("Error occured in: " + name)
        print(e)
        print(traceback.format_exc())
        quit(1)


def write_dummy(name, path, data_set):
    if is_test:
        print("Writing file: {}".format(path))

    xml_string = unicode("", 'utf-8')
    xml_string = xml_string + "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml_string = xml_string + "<letter xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n"
    xml_string = xml_string + "        xsi:noNamespaceSchemaLocation=\"../Schema_and_DTD/letter.xsd\"\n"
    xml_string = xml_string + "        title=\"" + unicode(name, 'utf-8') + "\"\n"
    xml_string = xml_string + "        catalogue_id=\"" + unicode(mc.get_system_number(data_set), 'utf-8') + "\"\n"
    xml_string = xml_string + "        date=\"" + unicode(mc.get_date(data_set), 'utf-8') + "\">\n"
    xml_string = xml_string + "   <metadata>\n"

    xml_string = xml_string + "      <!-- what comes here?! -->\n"

    # TODO ??? Does it need that?

    xml_string = xml_string + "   </metadata>\n"
    xml_string = xml_string + "   <persons>\n"

    authors = mc.get_author(data_set)
    xml_string = xml_string + "      <author>\n"
    xml_string = xml_string + unicode(get_person_xml_sting(authors), 'utf-8')
    xml_string = xml_string + "      </author>\n"

    recip = mc.get_recipient(data_set)
    xml_string = xml_string + "      <recipient>\n"
    xml_string = xml_string + unicode(get_person_xml_sting(recip), 'utf-8')
    xml_string = xml_string + "      </recipient>\n"

    mentioned = mc.get_mentioned_persons(data_set)
    mentioned_str = get_person_xml_sting(mentioned)
    if mentioned_str != "":
        xml_string = xml_string + "      <mentioned>\n"
        xml_string = xml_string + unicode(mentioned_str, 'utf-8')
        xml_string = xml_string + "      </mentioned>\n"

    xml_string = xml_string + "   </persons>\n"
    xml_string = xml_string + "   <text>\n"
    xml_string = xml_string + "      <p></p>\n"
    xml_string = xml_string + "   </text>\n"
    xml_string = xml_string + "</letter>\n"


    write_to_file(path, xml_string)
    return


def get_person_xml_sting(persons_list):
    if persons_list is None:
        return ""

    res = ""

    for person in persons_list:
        if person is None:
            res = res + "         <person/>\n"
            continue
        res = res + "         <person>\n"
        res = res + "            <gnd>{}</gnd>\n".format(person['GND'])
        res = res + "            <name>{}</name>\n".format(person['name'])
        res = res + "            <date>{}</date>\n".format(person['date'])
        res = res + "         </person>\n"

    return res


def write_to_file(path, data):
    #data = data.encode('utf-8')
    #data_u = unicode(data)
    #data_u = data.decode('utf-8')
    data_ascii = data.encode('utf-8')
    path_u = path.decode('utf-8')

    if is_test:
        print("Writing to File...\nData:\n{}".format(data_ascii))

    with codecs.open(path_u, "w", "utf-8") as f:
        f.write(data)

    print("Done Writing file.")
    return


def generate_name(data_set):
    # TODO handle unknown recipients

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
    #res = res.encode('utf-8')
    return res
