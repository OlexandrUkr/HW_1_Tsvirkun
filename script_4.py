set_1 = {11, 12, 32, 33, 1, 2, 3}
n1 = len(set_1)
text_1 = f'Введіть {n1} цифр, розділяючи їх комою з пробілом, рядок взяти в лапки ": '
list_2 = list(map(int, input(text_1).strip('"').split(',')))[:n1]
set_2 = set(list_2)
n2 = len(set_1 & set_2)
print("Кількість співпадань: ", n2)
