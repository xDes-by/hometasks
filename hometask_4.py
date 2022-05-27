# ====================================== task 1
def nothing():
    pass


# ====================================== task 2
def multiply(x):
    return x * 2


print(multiply(3))


# ====================================== task 3
def who_are_you(x):
    if x % 2 == 0:
        print("yes")
    else:
        print("no")


who_are_you(3)


# ====================================== task 4
def big(x, y):
    if x > 10:
        print("yes")
    else:
        print("no")


big(31, 5)

# ====================================== task 5
lamb = lambda y, z: y % z

print(lamb(3, 2))


# ====================================== task 6
def decor(func):
    def wrapper():
        c = 11
        func(c)

    return wrapper()


@decor
def show(a):
    x = 10
    g = a + x
    print(g)


# ====================================== task 6
ran = range(1, 5)


def num_x(x):
    return x * 2


num = list(map(num_x, ran))
print(num)

ran2 = range(1, 10)


def num_y(y):
    return y % 2


num2 = list(map(num_y, ran2))
print(num2)


# ====================================== task 7

def pure(x, y):
    return x + y


my_list = [1, 2, 3]


def dirty():
    x = 1
    my_list.append(x)


# ====================================== task 8

my_list_2 = [10, 2, 3]


def find_min_max():
    my_list_2.sort()
    return my_list_2[0], my_list_2[-1]


print(find_min_max())


# ====================================== task 9


def big_or_not_year(x):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        return True
    else:
        return False


year = int(input("Input year :"))
print(big_or_not_year(year))

# ====================================== task 10

year = {"spring": [3, 4, 5], "autumn": [9, 10, 11], "summer": [6, 7, 8], "winter": [1, 2, 12]}


def season(x):
    for k, v in year.items():
        if x in v:
            print(k)


numb = int(input("Input month number :"))
season(numb)

# ====================================== task 11
'''не ясно условие'''

# ====================================== task 12
new_list = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']
my_new_list = []


def sorty(x):
    for i in x:
        if type(i) == int or type(i) == float:
            my_new_list.append(i)
            my_new_list.sort()
    print(my_new_list)


sorty(new_list)
