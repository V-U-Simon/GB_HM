# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

"""Тут неободимо:
1. Выделение делением на 10
2. Определение через +/-"""



def my_round(number, ndigits):
    ten = 1
    for i in range(ndigits):
        ten = ten*10
    number = number * ten
    otb = int(number % 1 * 10)
    if otb >= 6:
        number += 1
    number = int(number) / ten
    return number

# round_list.append(number % 10)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_list = []
    while ticket_number > 0:
        ticket_list.append(ticket_number % 10)
        ticket_number = ticket_number // 10
    if sum(ticket_list[:3]) == sum(ticket_list[3:]):
        return 'билет счастливый'
    else:
        return 'билет НЕ счастливый'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
