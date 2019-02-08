from pymarc import MARCReader
from PyZ3950 import zoom
import os


force_all = False
is_test = False
no_list = []


def get_info_from_aleph(nos, force, test):
    print("Getting Meta Information from Aleph Catalogue...")
    print("Is Force Run: {}".format(force))
    global force_all
    force_all = force
    print("Is Test Run: {}".format(test))
    global is_test
    is_test = test
    global no_list
    no_list = nos

    res = []

    if is_test:
        res.append(test_mc())
    else:
        for no in no_list:
            res.append(get_marc(no))

    print("Done getting Meta Info.\n")
    return res


def get_marc(no):
    print("getting marc for: {}".format(no))

    if force_all:
        mc = read_mc(no)
        write_to_cache(mc, no)
        return mc

    if os.path.isfile("data/tmp/marc/" + no + ".marc"):
        return read_mc_from_cache(no)

    mc = read_mc(no)
    write_to_cache(mc, no)
    return mc


def read_mc_from_cache(no):
    with open("data/tmp/marc/" + no + ".marc", "rb") as f:
        data = f.read()
    reader = MARCReader(bytes(data), force_utf8=True, to_unicode=True)
    tmp = next(reader)
    return tmp


def write_to_cache(marc, no):
    with open("data/tmp/marc/" + no + ".marc", "wb") as f:
        data = bytearray(marc.data)
        f.write(data)


def test_mc():
    import random
    no = no_list[random.randint(0, len(no_list)-1)]
    print("Testing: {}".format(no))
    mc = read_mc(no)
    print(mc)
    write_to_cache(mc, no)
    print("date: {}".format(get_date(mc)))
    return mc


def read_mc(sys_no):
    print("reading: "+sys_no)

    try:
        conn = zoom.Connection('aleph.unibas.ch', 9909)
        conn.databaseName = 'dsv05'
        conn.preferredRecordSyntax = 'USMARC'

        query = zoom.Query('PQF', '@attr 1=1032 ' + sys_no)
        res = conn.search(query)
        data = bytes(res[0].data)
    except zoom.ConnectionError:
        print("\n!!! Error: could not connect to aleph !!!\n")
        return

    reader = MARCReader(bytes(data), force_utf8=True, to_unicode=True)
    tmp = next(reader)
    return tmp


def get_date(records):
    date = None
    for field in records.get_fields('046'):
        date = field['c']

    return date
