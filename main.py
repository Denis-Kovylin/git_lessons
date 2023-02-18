
# !!!!!!Homework with Python #2!!!!!!
# ----------------- Multiplication table for 3 -----------------------------
# --------------------------------------------------------------------------
# for i in range(1, 10):
#     print(f'3 * {i} = {3 * i}')
# --------------------------------------------------------------------------
# -----------------  AVG of numbers from 1 to 100 ----------------------------
# sum = 0
# for i in range(1, 101):
#     sum += i
#     average = sum/100
# print('The AVG of all numbers in the range 1 to 100 is:', average)

# sum_avg = sum(list(range(1, 101))) / 100
# print('The sum of all numbers in the range 1 to 100 is:', sum_avg)
# ---------------------------------------------------------------------------
# ----------- Divide by two until the result is less than fifty -----------
# number = float(input('Enter number: '))
# def divide_by_two(number):
#     if number < 50:
#         return 'You entered too low a number'

#     count = 0
#     while number >= 50:
#         number /= 2
#         count += 1

#     return f'Number of iterations: {count}, Number: {number}'

# result = divide_by_two(number)
# print(result)


















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
#     new_salary = 0
# elif work_experience < 1:
#     new_salary = salary * 1
# elif work_experience <= 3:
#     new_salary = salary * 1.1
# else:
#     new_salary = salary * 1.2

# if new_salary <= 0:
#     print('Invalid data!!!')
# elif new_salary == salary:
#     print('New salary: ', salary)
# elif new_salary < 4000:
#     new_salary += 1000
#     print('New salary: ', new_salary)
# else:
#     new_salary += 500
#     print('New salary: ', new_salary)




# salary = float(input('Enter your current salary: '))
# work_experience = float(input('Enter your work experience (years): '))
# new_salary = 0

# if salary <= 0 or work_experience <= 0:
#     new_salary = 0
# elif work_experience < 1:
#     new_salary = salary * 1
# elif 1 <= work_experience <= 3:
#     new_salary = salary * 1.1
# else:
#     new_salary = salary * 1.2

# if new_salary <= 0:
#     print('Invalid data!!!')
# elif new_salary >= 4000 and work_experience >= 1:
#     new_salary += 500
# elif new_salary < 4000 and work_experience >= 1:
#     new_salary += 1000
# else:
#     new_salary
# print('New salary: ', new_salary)


























# !!! УРОК ТРЕТИЙ !!!
# ----- Словари - неупорядоченые колекции объектов с доступом по ключу -----
# some_dict = {}
# # print(type(some_dict))
# some_dict["some_key"] = 123
# some_dict["some_text"] = 'Text'
# print(some_dict)
# # ----- Очищение словаря -----
# some_dict.clear()
# print(some_dict)
# # ----- Корирование словаря ----
# dict_1 = some_dict.copy()
# print(dict_1, some_dict)
# # ----- Перебор словаря (вариант 1) -----
# print(some_dict)
# for key in some_dict:
#     print(f'key: {key} value {some_dict[key]}')
#     # ----- Перебор словаря (вариант 2) -----
# print(some_dict)
# for key, values in some_dict.items():
#     print(f'Key: {key} value {values}')
# # ----- Метод values() выводит все значения из словаря -----
# print(some_dict.keys())

# some_dict.update({'some+1': '123.21', 'some_key': 123.23})
# print(some_dict)
# --------------------------------------------------------------
# ----- Класс - кастомный объект данных и этот объект может иметь некоторые функции внутри класса. Функции внутри класса будут являтся методами класса-----

# ---------------------------- АВТОМАТИЗАЦИЯ --------------------------------
# ---------------------------------------------------------------------------























# !!! УРОК ВТОРОЙ !!!
# --------- Оператор in проверяет, что объект содержит какой-то элемент ----------
# some_string = 'some text'
# print('o' in some_string)
# print('z' in some_string)
# -----------------------------------------------------------------------------------
# ----------- Оператор not - логическое отрицание ------------------------------------
# some_string = 'some text'
# # print('o' not in some_string)
# print(not('o' in some_string))
# print(not(2 > 3))
# -----------------------------------------------------------------------------------
# ------------ Метод len - возврашает длинну строки -----------------------------------
# some_string = "some text"
# print(len(some_string))
# print(len('Hello world'))
# -----------------------------------------------------------------------------------
# -------------- Обращение к итерабильному елементу через индекс (задается в [индекс]) -----
# some_string = "some text"
# print(some_string[3])
# -----------------------------------------------------------------------------------
# -------------- for переменная из объекта in итерабельный объект ---------------------
# some_string = "some text"
# for s in some_string:
#     print(s)
# for i in range(0, 10, 1):
#     print(i)
# -----------------------------------------------------------------------------------
# # Список чисел  ("от этого числа" до "этого числа" с шагом "в это число")
# for i in range(39, 1365, 13):
#     print(i)
# -----------------------------------------------------------------------------------
# Подсчет числа символов в строке
# lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pharetra
#  ligula id condimentum dapibus. Sed magna magna, hendrerit id tincidunt in, blandit a dui.
#   In turpis augue, vulputate nec dolor et, fermentum dictum sapien. Donec hendrerit semper
#    interdum. Mauris libero nisi, gravida eget eleifend eu, finibus ac tellus. Ut sed leo a
#     dolor scelerisque sodales bibendum non massa. Mauris diam enim, euismod venenatis
#      vehicula ut, suscipit ultrices ipsum. Vivamus faucibus massa massa, at rutrum urna
#       viverra id. Etiam nec velit euismod, interdum lectus sed, dignissim turpis. Mauris
#        ut eros metus. Vivamus rutrum, lectus aliquam imperdiet pharetra,
#         justo urna placerat metus, sodales auctor urna felis in ipsum. Donec vitae venenatis
#          eros. Aliquam elementum rhoncus tincidunt. Nam nec augue vehicula nulla porta
#           eleifend. Sed vel massa nec lectus finibus commodo. Sed sit amet metus nisl.
# Ut scelerisque lectus nibh, ac semper nibh finibus eget. Vivamus eget elementum ipsum. 
# Donec ornare libero non semper pretium. Donec ex ipsum, egestas ac enim eu, commodo
#  venenatis justo. Interdum et malesuada fames ac ante ipsum primis in faucibus.
#   Sed venenatis, eros id tempus fringilla, tellus arcu ullamcorper lectus, dapibus placerat
#    dui velit non nibh. Class aptent taciti sociosqu ad litora torquent per conubia nostra,
#     per inceptos himenaeos. Phasellus interdum nibh elementum, semper magna sed, consequat
#      nisl. Nulla id molestie ex. Quisque rhoncus lacinia sem, non varius tellus pretium a.
#       Proin ornare lacus erat, a fringilla lorem facilisis non. Etiam finibus,
#        sapien quis euismod eleifend, ligula sem vehicula magna, id elementum ex felis sit
#         amet eros. Maecenas et tortor tortor. Sed lobortis non velit eu pulvinar.
#          Aliquam sollicitudin tempor odio sit amet aliquet.
# Vivamus tellus nulla, pretium vel eros non, sodales mattis dolor. 
# Ut malesuada turpis ut est aliquam consequat. Proin sodales molestie mauris nec euismod. 
# Etiam nec tincidunt leo, eget finibus purus. Integer ut congue ante. 
# Proin sed lacus malesuada, auctor nisi sit amet, pretium lacus. 
# Donec nec justo nibh. Quisque at nunc ligula.
# In convallis, dui a pellentesque lobortis, dui nisi finibus dolor, vitae condimentum massa
#  leo vel lectus. Phasellus fringilla magna nec sapien ultricies congue. Suspendisse potenti.
#   Integer elementum sodales odio vitae tempus. Integer consectetur elit eu semper aliquam.
#    Nunc semper tincidunt vestibulum. Mauris suscipit enim justo, vitae dictum felis posuere
#     non. Integer ac luctus tellus, in volutpat lacus. Nullam sagittis ligula purus,
#      sit amet placerat elit euismod nec. Pellentesque risus nibh, tristique sit amet diam a,
#       euismod semper ligula. Sed pellentesque erat a dapibus molestie. 
#       Aenean scelerisque semper risus eget porttitor. 
#       Aenean molestie eu lectus non fermentum. Ut egestas auctor enim, quis pharetra dolor
#        placerat non.
# Suspendisse tempor erat eget quam facilisis rhoncus. 
# Mauris posuere odio ac ipsum tristique pellentesque. 
# Nam ullamcorper dui quis purus elementum vestibulum. Nulla facilisi. 
# Morbi pharetra purus metus, vel pretium est sodales et. 
# Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
#  Pellentesque sapien leo, pharetra ac scelerisque ut, egestas et enim. 
#  Pellentesque sit amet dolor quis arcu semper varius nec ac nunc. 
#  Proin ullamcorper, magna vitae finibus finibus, velit nibh blandit ipsum, nec 
#  maximus dolor elit eu ex."""

# print(len(lorem_ipsum))
# -----------------------------------------------------------------------------------
# Найти все числа которые нацело делятся на 4 в диапазоне от 100 до 400 (включительно)
# for i in range(100, 401):
#     if i % 4 == 0:
#         print(i)
# -----------------------------------------------------------------------------------
# Подсчет символов с цифровой разметкой
# some_string = "some text"
# for s in range(0, len(some_string)):
#     print(s, some_string[s])
# -----------------------------------------------------------------------------------
# Верхний/нижний регистр и разбивка с разделителем 
# some_string = "some text"
# # print(some_string.lower())
# # print(some_string.upper())
# # print(some_string.join())
# print(some_string.split('e'))
# -----------------------------------------------------------------------------------
# Удаление пробелов из строки
# some_string = "     Some text       "
# print(len(some_string), len(some_string.strip()))

# Удаление пробелов в строке справа
# some_string = "     Some text       "
# print(some_string.rstrip()) 

# Удаление пробелов в строке слева
# some_string = "     Some text       "
# print(some_string.lstrip()) 
# -----------------------------------------------------------------------------------
#--------Срезы - диапозон значений. Задается тремя цифрами в квадратных скобках-------
# --------[первое значение диарозона]:[второе значение диарозона]:[шаг диапазона]-------
# some_string = "Some text"
# print(some_string[0:4])
# -----------------------------------------------------------------------------------
# some_string = "some text"
# print(some_string[0:len(some_string):2])
# ------- Вывод строки -5 символов ------
# some_string = "some text"
# print(some_string[0:-5])
# ---Вывод строки в обратном порядке---
# some_string = "some text"
# print(some_string[::-1])
# ------- Поиск в строке - find (rfind, lfind)-------
# some_string = "some text"
# print(some_string.find('o'))
# print(some_string[some_string.find('o')])
# ------- Замена символа в строке - replace -------
# some_string = "some text"
# print(some_string.replace('o', 'new'))
# ------- Проверка строки на верний/нижний регистр - islower/isupper -------
# some_string = "some text"
# print(some_string.islower())
# print(some_string.isupper())
# --------- Проверка строки на цифры - isdigit -------
# some_string = "some text"
# print(some_string.isdigit())
# ------- Проверка строки на буквы с цифрами - isalnum --------
# some_string = "some text"
# print(some_string.isalnum())
# -------- Проверка строки на буквы - isalpha -------
# some_string = "some text"
# print(some_string.isalpha())
# -----------------------------------------------------------------------------------
# ------------------------- Списки ---------------------------------------
# -------- Вывод елементов списка -------
# some_list = [1, 32, 45, 'Test', [1.2, 342, 2.3]] 
# for ele in some_list:
#     print(ele)
# ------- Длинна списка --------
# some_list = [1, 32, 45, 'Test', [1.2, 342, 2.3]]
# print(len(some_list))
# -----------------------------------------------------------------------------------
# some_list = [1, 32, 45, 'Test', [1.2, 342, 2.3], 1.2, 342, 2.3]
# print(len(some_list))
# ------- Преоюразование строки в список - list() --------
# some_string = "some text"
# print(list(some_string))
# -------- Минимальное/максимальное значение списка - min()/max() ---------
# some_list = [1, 2, 3, 4, 5, 6]
# print(max(some_list), min(some_list))
# --------- Сумма объектов списка - sum() ---------
# some_list = [1, 2, 3, 4, 5, 6]
# print(sum(some_list))
# ---------- Добавление елемента в конец списка - append ---------
# some_list = [1, 2, 3, 4, 5, 6]
# some_list.append(23)
# print(some_list)
# ---------- Сортировка списка - sort() ---------
# some_list = [12, 7, 11, 8, 9, 10, 1, 2, 3, 4, 5, 6]
# some_list.sort()
# print(some_list)
# ----------- Вставка в список списка - insert() ---------
# some_list_insert = [1, 2, 3, 4, 5, 6]
# some_list = ['work', ['play'], ['sleep']]
# print(some_list.insert(1, some_list_insert))
# print(some_list)
# -------------------------------------------------------------
# ---------- Цикл с предусловием - while ------------
# some_list_insert = [21, 32, 1, 2, 3, 4, 5, 6]
# count = 0
# while len(some_list_insert) > count:
#     print(some_list_insert[count])
#     count += 1
# ------------ Цикл перебора до указаного числа ----------
# numb = True
# count = 0
# while numb:
#     if count == 120:
#         print(count)
#         break
#     else:
#         print(count)
#         count += 1
# ----------------- !!!continue!!! -----------
# numb = True
# count = 0
# while numb:
#     if count == 120:
#         print(count)
#         break
#     elif 10 < count < 110:
#         count += 1
#         continue
#     else:
#         print(count, end = " ")
#         count += 1
# -----------------------------------------------------------------
# -------------- Функции ------------
# Синтакси: def имя_функции(аргументы функции):
#                 тело функции
# --------- Функция с возвращаемым значением - return ---------
# def add(num_1, num_2):
#     sum = num_1 + num_2
#     return sum

# sum_1 = add(2, 8)
# print(sum_1)
# ------------------------------------------------------------------
# def add(num_1, num_2):
#     print(num_1 + num_2)

# add(2, 3)



    




























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