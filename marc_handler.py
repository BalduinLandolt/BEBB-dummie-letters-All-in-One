from pymarc import MARCReader
from PyZ3950 import zoom
import random


force_all = False
is_test = False
no_list = []


def get_info_from_aleph(list, force, test):
    print("Getting Meta Information from Aleph Catalogue...")
    print("Is Force Run: {}".format(force))
    global force_all
    force_all = force
    print("Is Test Run: {}".format(test))
    global is_test
    is_test = test
    global no_list
    no_list = list

    # TODO Do Stuff here
    test_mc()

    if is_test:
        res = test_mc()
    elif force_all:
        res = add_marcs_to_list([])
    else:
        cached = read_cached_marcs()
        res = add_marcs_to_list(cached)

    print("Done getting Meta Info.\n")
    return res


def read_cached_marcs():
    print("Reading cached marc data...")
     # TODO implement this


def add_marcs_to_list(prev):
    print("Getting new marc data...")
     # TODO implement this


def test_mc():
    no = "000054744"
    read_mc(no)


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

    print(data)
    reader = MARCReader(bytes(data), force_utf8=True, to_unicode=True)
    print(reader)
    tmp = next(reader)
    print(tmp)
    print("date:")
    print(get_date(tmp))
    return tmp


def get_date(records):
    date = None
    for field in records.get_fields('046'):
        date = field['c']

    return date
