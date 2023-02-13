# !!!!!!Homework with Python #1!!!!!!

# -----------AGE_VALIDE---------------
# age = int(input('Enter your age: '))
# if age < 0:
#     print('Invalid age')
# elif age < 18:
#     print('You are not yet an adult')
# else:
#     print('You are now an adult')
# # --------------------------------------

# # --------------A_divid_B------------------
# a = int(input('Enter first numeric: '))
# b = int(input('Enter second numeric: '))

# if a % b == 0:
#     print('Divides evenly. Result of division is:', int(a / b))
# else:
#     print('Divides with a remainder. Remainder is:', a % b)
# ------------------------------------------------

# # ---------------Pay_Roll-----------------------
# salary = float(input('Enter your current salary: '))
# work_experience = float(input('Enter your work experience (years): '))
# new_salary = 0

# if salary <= 0 or work_experience < 0:
#     new_salary = False
# elif work_experience < 1:
#     new_salary = salary 
# elif work_experience <= 3:
#     new_salary = salary * 1.1
# else:
#     new_salary = salary * 1.2

# if new_salary == False:
#     print('Invalid data!!!')
# elif new_salary < 4000:
#     new_salary += 1000
#     print('New salary: ', new_salary)
# else:
#     new_salary += 500
#     print('New salary: ', new_salary)








# !!!!!!Homework with Python #2!!!!!!
# for i in range(1, 10):
#     print(f"3 * {i} = {3 * i}")




























# !!! УРОК ВТОРОЙ !!!

# Длинна строки
# some_string = "some text"
# print(len(some_string))

# Текст вертикально
# some_string = "some text"
# for s in some_string:
#     print(s)

# # Список чисел  ("от этого числа" до "этого числа" с шагом "в это число")
# some_string = "some text"
# for i in range(39, 1365, 13):



# for s in range(0, len(some_string)):

# # На  ти все числа которые нацело делятся на 4 в диапазоне 100 - 400
# for i in range(100, 401):
#     if i % 4 == 0:
#         print(i)

# Подсчет символов с цифровой разсеткой
# some_string = "some text"
# for s in range(0, len(some_string)):
#     print(s, some_string[s])

# Верхний/нижний регистр и разбивка с разделителем 
# some_string = "some text"
# print(some_string.lower())
# print(some_string.upper())
# print(some_string.split())

# some_string = "     Some text       "
# print(len(some_string), len(some_string.strip()))

# Срезы - диапозон значений. Задается тремя цифрами в квадратных скобках
# some_string = "some text"
# print(some_string[0:5])
# some_string = "some text"
# print(some_string[0:len(some_string):2])
# some_string = "some text"
# print(some_string[0:-1])
# ---Вывод строки в обратном порядке---
# some_string = "some text"
# print(some_string[::-1])

# some_string = "some text"
# print(some_string.find('o'))
# print(some_string[some_string.find('o')])


# ---Списки---
# some_list = [1, 32, 45, 'Test', [1.2, 342, 2.3]]  - вложеные списки
# for ele in some_list:
#     print(ele)

# some_list = [1, 32, 45, 'Test', [1.2, 342, 2.3]]
# print(len(some_list))
# some_string = "some text"
# print(list(some_string))

# some_list = [1, 32, 45, 'Test', [1.2, 342, 2.3], 1.2, 342, 2.3]

# some_list_insert = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 88]
# some_list = ['work', 'play', 'sleep']
# # print(min(some_list))
# # print(max(some_list))
# print(some_list.insert(1, some_list_insert))




# while c предустовием
# count = 0
# while len(some_list_insert) > count:
#     print(some_list_insert[count])
#     count += 1

# Бесконечный цикл
# is_number = True
# count = 0
# while is_number:
#     print(count)
# #     count += 1

# cont = 0 
# is_number = True
#     if count ==120:
#         print(cont)
#         break
#     elif 10 < 110:
#         # print(count, end=" ")
#         cont += 1
#         continue
#     else:
#         print(cont, end=" ")
#         cont += 1
    




























# !!! УРОК ПЕРВЫЙ !!!

# int - целые числа
# float - дробные числа
# bool - бинарный тип: True/False
# str - строка (Всегда оборачивается в кавычки "")

# type - показывает тип данных
# text = 123
# print(text)
# print(type(text))

# text = 123
# print(text)
# print(type(text))

# text = 123.33
# print(text)
# print(type(text))

# text = True
# print(text)
# print(type(text))

# text = "123"
# print(text)
# print(type(text))


# escapa последовательности
# \t - табуляция
# \n - пренос на новую строку

# text = "Привет\t123 \n как дела?"
# print(text)

# input() - позволяет вводить данныу из консоли в код
# some_text = input("Enter some text")
# print(some_text)

# Форматирования строк
# Ф-строки
# name = input(" Enter your name: ")
# print(" Hello " + name)
# age = int(input(" Enter your age: "))
# print(f' your age is {age} year old ')
# print(type(age))
# ----------------------------------------
# name = input(" Enter your name: ")
# age = int(input(" Enter your age: "))
# print(' your name {} your age is {} '.format(name, age))
# print(type(age))
# ----------------------------------------------
# name = input(" Enter your name: ")
# age = int(input(" Enter your age: "))
# print(' your age is {1} your name is {0} '.format(name, age))
# print(type(age), type(name))
# ----------------------------------------
# name = input(" Enter your name: ")
# # age = int(input(" Enter your age: "))
# some_list = [1, 2, 3, 45, 5, 6, 74, 8, 9, 10]
# print(' your age is {1} your name is {0} '.format(name, age))
# print(type(age), type(name))
# ----------------------------------------
# some_list = ["text", "test", "some", "45", "3"]
# some_list = [1, 2, 4, 45, 3]
# # print('last element {4}, first element {0}, other elements {1}, {2}, {3}'.format(some_list[0], some_list[1], some_list[2], some_list[3], some_list[4]))
# # print(f'last element {some_list[4]}, first element {some_list[0]}, other elements {some_list[1]}, {some_list[2]}, {some_list[3]}')
# print('last element {}, first element {}, other elements {}, {}, {}'.format(some_list[0], some_list[1], some_list[2], some_list[3], some_list[4]))



# Перенос длинных строк
# text = " Hello " \
#     "World"
# print(text)
# text = ("Проснувшись однажды утром после беспокойного сна, Грегор"
# " Замза обнаружил, что он у себя в постели превратился в страшное насекомое. Лежа на панцирнотвердой спине, он"
# " видел, стоило ему приподнять голову, свой коричневый, выпуклый, разделенный дугообразными чешуйками живот, на верхушке
# " которого еле держалось готовое вот-вот окончательно сползти одеяло. Его многочисленные, убого тонкие")
# text = '''  однажды утром после беспокойного сна,
#  Грегор Замза обнаружил, что он у себя в постели превратился в страшное
#   насекомое. Лежа на панцирнотвердой спине, он видел, стоило ему приподнять голову
#   , свой коричневый, выпуклый, разделенный дугообразными чешуйками живот, на верхушке 
#   которого еле держалось готовое вот-вот окончательно сползти одеяло. Его многочисленные
#   , убого тонки '''
# print('Проснувшись однажды утром после беспокойного сна, Грегор Замза обнаружил, что он у себя в постели превратился в страшное насекомое. Лежа на панцирнотвердой спине, он видел, стоило ему приподнять голову, свой коричневый, выпуклый, разделенный дугообразными чешуйками живот, на верхушке которого еле держалось готовое вот-вот окончательно сползти одеяло. Его многочисленные, убого тонкие по сравнению с остальным телом ножки беспомощно копошились у него перед глазами. «Что со мной случилось?» – подумал он. Это не было сном. Его комната, настоящая, разве что слишком маленькая, но обычная комната, мирно покоилась в своих четырех хорошо знакомых стенах. Над столом, где были разложены распакованные образцы сукон – Замза был коммивояжером, – висел портрет, который он недавно вырезал из иллюстрированного журнала и вставил в красивую золоченую рамку. На портрете была изображена дама в меховой шляпе и боа, она сидела очень прямо и протягивала зрителю тяжелую меховую муфту, в которой целиком исчезала ее рука. Затем взгляд Грегора устремился в окно, и пасмурная погода – слышно было, как по жести подоконника стучат капли дождя – привела его и вовсе в грустное настроение. «Хорошо бы еще немного поспать и забыть всю эту чепуху», – подумал он, но это было совершенно неосуществимо, он привык спать на правом боку, а в теперешнем своем')

# print(' some text ', end=' ')
# print(' some other text ')

# name = 'Denis'
# age = 37
# print(f'My name is {name} and my age is {age}')




# Матекматические операции: -,+,*,/
# result = (2+2*2-2/2)
# print(result)
# print(type(result))
# -----------------------------------------------------
# result = 2**5
# print(result)
# print(type(result))
# -----------------------------------------------------
# % - Результат остатка от деления
# result = 10%3
# print(result)
# print(type(result))
# -----------------------------------------------------
# // - Целочисленное деление
# result = 10//4
# print(result)
# print(type(result))
# -----------------------------------------------------
# str_1 = ' Some Text '
# str_2 = ' Some other text '
# print( str_1 + str_2 )


# Условия. Логические операторы: <,>,=,<=,>=,==,!=
# print( 2 < 3, type( 2 < 3 ))
# print( 2 > 3, type( 2 > 3 ))
# -------------------------------------------
# print( 'Oleg' < 'oleg' )
# -------------------------------------------
# print(2==2)
# print(2!=3)



# Условные операторы if elif else
# name = 'Denis'
# if name == 'Denis':
#     print( f'Hello  {name}')
# -------------------------------------
# name = 'Den'
# if name == 'Denis':
#     print( f'Hello  {name}')
# # elif name != 'Denis':
# #     print( f'{name} WHO ARE YOU???')
# else:
#     print('Access denied! ')
# print('end')
# -------------------------------------
# name = 'Den'
# if type(name) == str and name == 'Denis':
#     print( f'Hello  {name}')
# elif name != 'Denis':
#     print(type(name) == str and name == 'Denis', name)
#     print( f'{name} WHO ARE YOU???')
# else:
#     print('Access denied! ')
# print('end')
# -------------------------------------
# name = 'Den'
# if type(name) == str:
#     if name == 'Denis':
#      print( f'Hello  {name}')
#     elif name != 'Denis':
#      print(type(name) == str and name == 'Denis', name)
#     print( f'{name} WHO ARE YOU???')
# else:
#     print('Access denied! ')
# -------------------------------------
# name = 'Den'
# if type(name) == str:
#     print('This is string')

# if name == 'Denis':
#     print( f'Hello  {name}')
# else:
#     print('You no a Denis')

# if name != 'Denis':
#     print( f'{name} WHO ARE YOU???')

# if type(name) != str:
#     print('Access denied! ')
# else:
#     print(f'Type is {type(name)}')
# -------------------------------------
# name = 'Den'
# if name == 'Denis' and type(name) == str:
#     print( f'Hello  {name}')
# elif type(name) == int and name != 'Denis':
#     print(type(name) == str and name == 'Denis', name)
#     print( f'{name} WHO ARE YOU???')
# else:
#     print('Access denied! ')
# ------------------------------------