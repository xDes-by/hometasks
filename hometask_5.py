'''
первое задание по типизации в файле hometask_4.py
'''


# ====================================================== TASK 2

def some(x: int, n: int, a: str) -> any:
    result: str = str(x + n) + a
    return result


print(some(2, 6, " dodo pizza"))


# ====================================================== TASK 3

def task_3(x: str) -> int:
    return print(x)


task_3("hello my friend")

# ====================================================== TASK 4
x: int = 3
y: int = 4


def decor(func):
    def wrapper():
        print("Степень суммы чисел x,y равна", func() ** 2)

    return wrapper


@decor
def task_4():
    z = x + y
    return z


task_4()

# ====================================================== TASK 5

my_list: list = [1, 33, "ew", 98, "po", 198, "ye"]


def check():
    for i in my_list:
        yield i


def take_elem():
    numb = 0
    for i in my_list:
        numb += 1
        if numb == 5:
            print(next(elem))
        else:
            next(elem)


elem = check()
take_elem()
