"""
есть ли способ переобразовать str в математический символ? если есть то калькулятор займет строк 5 макс,
и еще пробовал через eval() но как по мне бред

черепаха и дополнительные задания в другий файлах
"""

number_1 = int(input("Введите число: "))
operator = input("Введите действие: ")
number_2 = int(input("Введите число: "))

result = ''
if operator == "*":
    result = number_1 * number_2
elif operator == "/":
    result = number_1 / number_2
elif operator == "-":
    result = number_1 - number_2
elif operator == "+":
    result = number_1 + number_2
else:
    print("а больше я ничего не умею=)")

print(result)

# ======================= 2 ВАРИАНТ ======================
result = ''
while True:
    task = input("Введите уравнение c '+','-','*' или '/': ")
    if "*" in task:
        number_list = task.split("*")
        result = int(number_list[0]) * int(number_list[1])
    elif "-" in task:
        number_list = task.split("-")
        result = int(number_list[0]) - int(number_list[1])
    elif "+" in task:
        number_list = task.split("+")
        result = int(number_list[0]) + int(number_list[1])
    elif "/" in task:
        number_list = task.split("/")
        result = int(number_list[0]) / int(number_list[1])
    else:
        print("Мне такое не подходит, ухожу в тень...")
        break
    print(result)