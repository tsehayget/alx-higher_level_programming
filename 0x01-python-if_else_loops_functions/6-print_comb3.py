#!/usr/bin/python3
for a in range(10):
    for i in range(a + 1, 10):
        print("{}".format(str(a) + str(i)), end="")
        if int(str(a) + str(i)) < 89:
            print(", ", end="")
print("")
