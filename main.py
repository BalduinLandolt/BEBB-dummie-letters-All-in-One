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


print("Done.")