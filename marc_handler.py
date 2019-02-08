from pymarc import MARCReader
from PyZ3950 import zoom


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

    # TODO Do Stuff here

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
    import random
    no = no_list[random.randint(0, len(no_list)-1)]
    print("Testing: {}".format(no))
    mc = read_mc(no)
    print(mc)
    print("date: {}".format(get_date(mc)))


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
