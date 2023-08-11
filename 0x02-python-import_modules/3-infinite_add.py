#!/usr/bin/python3
def add_arg(argv):
    k = len(argv) - 1
    if k == 0:
        print("{:d}".format(k))
        return
    else:
        i = 1
        add = 0
        while i <= k:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)

