#!/usr/bin/python3
for d in range(ord('a'), ord('z') + 1):
    if d != ord('e') and d != ord('q'):
        print("{:d}".format(d), end="")
