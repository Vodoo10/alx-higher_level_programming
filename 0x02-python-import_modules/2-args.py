#!/usr/bin/python3
# Function
sh: 1: q: not found
    import sys

    arg = sys.argv
    i = len(arg) - 1

    if i >  0:
        print("{} arguments:".format(i))
        for k in range(1, i + 1):
            print("{}: {}".format(k, arg[k]))

    elif i == 0:
        print("{} arguments.".format(i))

    else:
        print("{} argument:".format(i))
        print("{}: {}".format(i, arg[1]))
