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
# range(1,100) диапозо

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

my_str1="Qwerty"
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
# new_str=my_str1[::-1]    # разворот строки
# if my_str1[-1]=="a":
#     print(f'последняя буква a в строк: {my_str1}')
# else:
#     print(f'последняя буква не a в строк: {my_str1}')
# print(str_len, new_str)

# циклы
# for symbol in my_str1:
#     if symbol in "EYUIOAeyuioa":
#         print(symbol)
# for symbol in my_str1:
#     if (symbol not in "EYUIOAeyuioa") and symbol.isalpha():  # isalpha() проверка на буквы
#         print(symbol)

# for symbol in my_str1:
#     if (symbol not in "EYUIOAeyuioa") and symbol.isalpha() and symbol.isupper():
#         print(symbol)

# for symbol in my_str1:
#     print(f"symbol '{symbol}' --> {ord(symbol)}")

# for index in range(100):
#     print(f"index: '{index}' --> '{chr(index)}")

# for index in range(32,ord('z')+1, 2):
#     print(f"index: '{index}' --> '{chr(index)}")

count=0
# while count < 10:
#     print('hello')
#     count += 1
# do_loop= True
# while do_loop:
#     print('hello')
#     count += 1
#     if count>= 5:
#         do_loop=False

from random import randint

# comp_value=randint(1, 10)
# go_game = True
# while go_game:
#     cur_value=int(input("угадай число от 10 до 10:"))
#     if cur_value == comp_value:
#         go_game=False
#         print("Победа!")

# value=input("Введи число")
# try:
#     value_int=int(value)
#     result=value_int*10
#     print(result)
# except ValueError:
#     print("Єто не число")
# except ZeroDivisionError:
#     print("на 0 нельзя")

# my_str="qwErty123"
# for symbol in my_str:
#     # if symbol.isalpha():
#     if symbol.lower() in "eyuioa":
#         print(symbol)

# tuple кортежи и list - списки

my_tuple=(1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"]) # не изменяевмий тип данних
my_list= [1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"]] # изменяевмий тип данних
# print(my_list, type(my_list))
# print(my_tuple, type(my_tuple))
# index=1
# print(my_tuple[index])
# print(len(my_tuple))

# new_list=my_list[1::2]
# print(new_list)
# for value in my_list:
#     print(value)

# my_list[0]=56
# my_tuple=(100, *my_tuple[1:])  # * - распаковка кортежа и списка
# print(my_tuple)

# val_1=12
# val_2=21
# val_2, val_1 = val_1, val_2
# item= val_2, val_1
# print(val_1, val_2)
# print(item)
# list_1= [1, 2]
# list_2= [3, 4]
# # new_list= [list_1, list_2]
# new_list= [list_1, list_2[:]] # срез [:] - срез всегда копия данних
# print(new_list)
# list_1[0]= 100
# list_2[0]= 300
# print(new_list)

#############
# new_list= []
# for symbol in "qwerty":
#     new_list.append(symbol)
# print(new_list)
# new_list.append(1000)
# print(new_list)
# # new_list.pop()   # вырезает элемент .... () последний элемент
# new_list.pop(4)  # вырезает элемент .... (4) 4 элемент
# result= new_list.pop(4)
# print(result)

# new_list= list("qwerty")
# new_list_1= ["qwerty"]
# print(new_list)
# print(new_list_1)
# new_list= list("qwerty")
# print(new_list)
# new_str= "$".join(new_list)
# print(new_str)

file_name= "lesson1.txt"
# file_name= file_name.replace(".txt", "")
# file_name= file_name.split(".")
# print(file_name)
# file_name= file_name[:-1]
file_name= file_name.rsplit(".", 1)[0]    # rsplit() сплит справа до 1 точки
print(file_name)