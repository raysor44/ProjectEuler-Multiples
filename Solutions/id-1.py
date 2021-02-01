import sys


def Multiples(index, sum):
    while True:
        index += 1

        if index < 1000:  # Find sum of all the multiples below 1000
            if index % 3 == 0 or index % 5 == 0:
                sum += index
                print("index =", index, " | ", "sum =", sum)
        else:
            sys.exit(0)  # Exit if program ended


Multiples(0, 0)
