import sys


def Multiples():
    n = 0
    sum = 0

    while True:
        n += 1

        if n < 1000:  # Find sum of all the multiples below 1000
            if n % 3 == 0 or n % 5 == 0:
                sum += n
                print("n =", n, " | ", "sum =", sum)
        else:
            sys.exit(0)  # Exit if program ended


Multiples()
