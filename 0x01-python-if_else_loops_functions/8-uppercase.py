#!/usr/bin/python3
def uppercase(str):
    t = list(str)
    for a in range(len(t)):
        if (ord(t[a]) > 96 and ord(t[a]) < 123):
            t[a] = chr(ord(t[a]) - 32)
    print(("{}".format(("").join(t))))
