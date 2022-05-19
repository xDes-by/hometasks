names = ['Alex', 'Olga', 'Max', 'Dasha']
print(names[1], names[3])

# =========================================================

names_2 = {'Alex': 'man', 'Olga': 'woman', 'Max': 'man', 'Dasha': 'woman'}
new_names_list = [key for key, value in names_2.items() if value == 'woman']
print(new_names_list)

# =========================================================

numbers = [1, 8, 26, 598, 59, 4445, 9, 77896]
new_list = [i for i in numbers if len(str(i)) % 2 == 1]
print(new_list)
