# ======================================= TASK 1
my_list = [12, 0, 5, 0, 0, 8, 9]

for i in range(len(my_list)):
    if my_list[i] == 0:
        if my_list[i] == my_list[i+1]:
            print("Есть 2 нуля подряд!")
            print("=====================================================")

# ======================================= TASK 2
my_list_2 = [0, 2, 5, 1, 0, 8, 9]

for i in range(len(my_list_2)):
    if my_list_2[i] == 0:
        if i >= 2:
            my_list_2[i] = my_list_2[i-1]+my_list_2[i-2]
        elif i == 1:
            my_list_2[i] = my_list_2[i-1]
        else:
            continue

print(my_list_2)
print("=====================================================")

# ======================================= TASK 3
my_list_3 = [8, -1, 2, -5, 1, -3, 3, -9]

my_list_positive =[]
my_list_negative = []

for i in my_list_3:
    if i < 0:
        my_list_negative.append(i)
    else:
        my_list_positive.append(i)

print(my_list_positive)
print(my_list_negative)
print("=====================================================")

# ======================================= TASK 4
my_list_4 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
new_list = []

for i in range(len(my_list_4)):
    if my_list_4[i] != 0:
        new_list.append(my_list_4[i])
        if my_list_4[i] <= 0:
            new_element = my_list_4[i] ** 2
            new_list.append(new_element)

new_list.reverse()
print(new_list)
print("=====================================================")

