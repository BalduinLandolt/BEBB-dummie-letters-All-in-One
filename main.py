"""
Run this, to get the whole dummie-process going.

Possible arguments (not case sensitive):
none: runs a regular run.
"test": runs a test run, that just creates a hand full of dummies. Should be fairly quick.
"force": runs a force run, that ignores tasks that are done already.

"""

print("Strating...")

import sys

print("running with ({}) Arguments: {}".format(len(sys.argv), sys.argv))

is_test = False
force_all = False

if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    print("Analyzing Argument: {}".format(arg))
    is_test = (arg == "test")
    force_all = (arg == "force")

print

if is_test:
    print("##### Test Run #####")
elif force_all:
    print("##### Force Complete Run #####")
else:
    print("##### Regular Run #####")

print

import number_handler
import marc_handler
import dummie_writer

number_list = number_handler.get_sys_nos_to_work_with(force_all, is_test)

marc_handler.get_info_from_aleph(number_list, force_all, is_test)

dummie_writer.write_dummies(force_all, is_test)

print("Done.")
