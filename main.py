# Пользователь вводит число. Определить количество цифр в этом числе,
# посчитать их сумму и среднее арифметическое. Определить количество
# нулей в этом числе. Общение с пользователем организовать через меню.

# while True:
#     a = int(input('A or -1')) # 1234
#     counter_number = 0
#     counter_zero = 0
#     summa = 0
#     while a > 0:
#         summa += a % 10
#         counter_number += 1
#         if a % 10 == 0:
#             counter_zero += 1
#         a = a // 10
#     if a == -1:
#         print("Exit")
#         break
#     print(f'Count number {counter_number}\n'
#           f'Summa = {summa}\n'
#           f'Even = {summa / counter_number}\n'
#           f'Count zero = {counter_zero}')
while True:
    a = input('A or -1')
    summa = 0
    count_zero = 0
    count_number = 0
    for i in a:
        count_number += 1
        summa += int(i)
        if i == "0":
            count_zero += 1
    print(f'Count number {count_number}\n'
          f'Summa = {summa}\n'
          f'Even = {summa / count_number}\n'
          f'Count zero = {count_zero}')
    if a == "0":
        print("Exit")
        break
