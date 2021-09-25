# print("hello, world")
# ctrl+alt+L форматирует код под стандарт PEP8
# ctrl+/    комментировать строки
# == сравнениие
# != не равно
# in проверка на содержание в строке символа
# not  инверсия
# float(), int(), str(), bool()  функции приведения типов
# if not x%2 - проверка на четность
# len длина строки
# from random import randint # функция получения случайного числа
# тернарный оператор - result=case**2 if case>3 else -case
# new_str=my_str1[::-1]    # разворот строки

value = 5
test = '2'
# test, value = value, test
# value_1 = test / value # стандартное деление чисел
# value_1 = test // value # целочисленное деление (без округления )
# value_1=test%value # остаток от деления
# value_1 = test ** value  # возведение в степень
# value_1=test*value # склейка переменных если символ умножить на число
# print(value*test)
# bool_value=2
# bool_value_1=(2==bool_value)
# bool_value_1=("qwe" in "qwerty")
# bool_value_1=("qwe" not in "qwerty")
# bool_value_1=("qwef" in "qwerty")
# bool_value_2=not bool_value_1
# print(bool_value_2)

# value=1.80
# value='sss'
# value_bool=bool(value)  # всегда Т, кроме значения 0 и 0.0 и "" (пустая строка) - всегда F
# print(value_bool)

######################
# temp=14
# if temp>12:
#     print("тепло")
#     print(temp)
# else:
#     print("холодно")

# case=6
# if case==6:
#     print("победа Васи")
# else:
#     print("Все проиграли")
# case=7
# if case==6:
#     print("победа Васи")
# elif case==1:
#     print("победа Пети")
# else:
#     print("Все проиграли")

# case=input("кинь кубик:") # всегда str
# case=int(case)
from random import randint # функция получения случайного числа
# case=randint(1,6)
# print(case)
# if case==6:
#     print("победа Васи")
# elif case==1:
#     print("победа Пети")
# else:
#     print("Все проиграли")

# case=randint(1,6)
# print(case)
# if case>3:
#     print(case**2)
# else:
#     print(-case)

# тернарный оператор
# result=case**2 if case>3 else -case
# print(result)

##########
# строки и методы строк
# форматирование строк
# case=1
# result=2
# print(f"выпало число:{case} с результатом:{result}")

# dirname="home"
# filename="test.txt"
# path=f"{dirname}/{filename}"
# print(path)

# my_str1="qwerty"
# index=3           # -1 последний с конца строки
# symbol=my_str1[index]
# print(symbol)
# str_len=len(my_str1)  # len длина строки
# new_str=my_str1[0:4]   # часть строки: от левого индекса (включительно) до правого (не включается)
# new_str=my_str1[:]     # вся строка
# new_str=my_str1[:3]    # от начала до 3
# new_str=my_str1[2:]    # от 2 до конца
# new_str=my_str1[0:index]+"k"+my_str1[index+1:]
# new_str=my_str1[2:5:2]    # от 2 до 5 c шагом 2
new_str=my_str1[::-1]    # разворот строки
print(str_len, new_str)
