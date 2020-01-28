#!/usr/bin/python3
count = 1
for i in range(122, 96, -1):
    if count % 2 == 1:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
    count += 1
