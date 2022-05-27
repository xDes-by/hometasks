import datetime
import time

# ======================================= task 1
list_1 = [1, 2, 3]
list_2 = ["a", "b", "c", "d"]


def collect(x, y):
    z = x + y
    print(z)


collect(list_1, list_2)

# ======================================= task 2
list_1 = [1, 2, 3]


def collect(x):
    x.sort()
    max_numb = x[-1]
    print(max_numb)


collect(list_1)


# ======================================= task 3

def days():
    da = time.strftime("%a:%H:%M:%S")
    print(da)


days()

# ======================================= task 4

list_3 = ["a", "b", "c", "d"]


def rev(x):
    x.reverse()
    return x


print(rev(list_3))
