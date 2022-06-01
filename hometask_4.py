from typing import Union, List


# ====================================== task 1
def nothing():
    pass


# ====================================== task 2
def multiply(x: Union[int, float]) -> int:
    return x * 2


print(multiply(3))


# ====================================== task 3
def who_are_you(x: Union[int, float]):
    if x % 2 == 0:
        print("yes")
    else:
        print("no")


who_are_you(3)


# ====================================== task 4
def big(x: Union[int, float], y: Union[int, float]):
    if x > 10:
        print("yes")
    else:
        print("no")


big(31, 5)

# ====================================== task 5
lamb_1 = lambda y, z: y % z

y: int = 3
z: int = 2

print(lamb_1(y, z))


# ====================================== task 6
def decor(func):
    def wrapper():
        c: int = 11
        func(c)
        print("sad")

    return wrapper()


@decor
def show(a: int):
    x: int = 10
    g = a + x
    print(g)


# ====================================== task 6
ran: List[int] = [1, 2, 3, 4, 5]


def num_x(x: int) -> int:
    return x * 2

'''
тут по идее не надо объявлять, ведь мы и так создаем список
'''
num: list = list(map(num_x, ran))
print(num)

ran2 = range(1, 10)


def num_y(y: int):
    return y % 2

'''
тут по идее не надо объявлять, ведь мы и так создаем список
'''
num2: list = list(map(num_y, ran2))
print(num2)


# ====================================== task 7

def pure(x: int, y: int) -> int:
    return x + y


my_list: list[int] = [1, 2, 3]


def dirty():
    x: int = 1
    my_list.append(x)


# ====================================== task 8

my_list_2: list[int] = [10, 2, 3]


def find_min_max():
    my_list_2.sort()
    return my_list_2[0], my_list_2[-1]


print(find_min_max())


# ====================================== task 9


def big_or_not_year(x: int):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        return True
    else:
        return False


year = int(input("Input year :"))
print(big_or_not_year(year))

# ====================================== task 10

year_2: dict = {"spring": [3, 4, 5], "autumn": [9, 10, 11], "summer": [6, 7, 8], "winter": [1, 2, 12]}


def season(x: int):
    for k, v in year_2.items():
        if x in v:
            print(k)


numb = int(input("Input month number :"))
season(numb)

# ====================================== task 11
'''не ясно условие'''

# ====================================== task 12
new_list: list = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']
my_new_list: list[Union[int, float]] = []


def sorty(x: list):
    for i in x:
        if type(i) == int or type(i) == float:
            my_new_list.append(i)
            my_new_list.sort()
    print(my_new_list)


sorty(new_list)
