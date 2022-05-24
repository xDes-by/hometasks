# =============================== task 1 ===============================
a = 1
count = 2
user_number = int(input("Введите число :"))
while count != user_number:
    a = a * count
    count += 1
print(a)

# =============================== task 2 ===============================
numb1 = 0
numb2 = 1

n = int(input("Cколько :"))
i = 0

list_numb = []
while i < n:
    list_numb.append(numb1)
    numb1, numb2 = numb2, numb2 + numb1
    i = i + 1
print(list_numb)

# ---------------------
a = 1
b = 1
n = int(input("Cколько :"))
list_numb = []

for i in range(n):
    list_numb.append(a)
    a, b = b, a + b
print(list_numb)

# =============================== task 3 ===============================
numb = input("Введите число: ")
my_list = list(numb)
my_list.reverse()
numb2 = "".join(my_list)
print("Обратное число: ", numb2)

# ---------------------------

numb = input("Введите число: ")
numb2 = numb[::-1]
print("Обратное число: ", numb2)

# ================================ task 4 ================================

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    elif i % 5 == 0:
        print("Buzz", i)

# ================================ task 5 ================================

numb = input("Введите число: ")
my_list = list(numb)
my_list.sort()
numb2 = my_list[-1]
print("Наибольшее число: ", numb2)