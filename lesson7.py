#Практичне завдання 7.1
"""Розробити класс Sphere для представлення сфери у тривимірному просторі.

Забезпечити наступні методи класу:

конструктор, який приймає 4 дійсних числа: радіус, та 3 координати центру кулі. Якщо конструктор викликається без аргументів, створити об'єкт сфери із одиничним радіусом та центром у початку координат. Якщо конструктор викликається з 1 аргументом, створити об'єкт сфери з відповідним радіусом та центром у початку координат.
метод get_volume(), який повертає дійсне число -- об'єм кулі, обмеженої поточною сферою.
метод get_square(), який повертає дійсне число -- площу зовнішньої поверхні сфери.
метод get_radius(), який повертає дійсне число -- радіус сфери.
метод get_center(), який повертає тьюпл із 3 дійсними числами -- координатами центра сфери в тому ж порядку, в яком вони задаються в конструкторі.
метод set_radius(r), який приймає 1 аргумент -- дійсне число, та змінює радіус поточної сфери, нічого не повертаючи.
метод set_center(x,y,z), який приймає 3 аргументи -- дійсних числа, та змінює координати центра сфери, нічого не повертаючи. Координати задаються в тому ж порядку, що і в конструкторі.
метод is_point_inside(x,y,z), який приймає 3 аргументи -- дійсних числа -- координати деякої точки в просторі (в тому ж порядку, що і в конструкторі), та повертає логічне значення True або False в залежності від того, чи знаходиться ця точка всередині сфери.
Тести із некорестними даними не проводяться.

Приклад послідовності дій для тестування класу:
s0 = Sphere(0.5) # test sphere creation with radius and default center
print s0.get_center() # (0.0, 0.0, 0.0)
print s0.get_volume() # 0.523598775598
print s0.is_point_inside(0, -1.5, 0) # False
s0.set_radius(1.6) 
print s0.is_point_inside(0, -1.5, 0) # True
print s0.get_radius() # 1.6"""

import math

class Sphere(object):

    def __init__(self, r = 1, x = 0.0, y = 0.0, z = 0.0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z


    def get_volume(self):
        return math.pi * self.r ** 3 * 4 / 3
    

    def get_square(self):
        return 4 * math.pi * self.r ** 2

    def  get_radius(self):
        return self.r

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, rad):
        self.r = rad

    def set_center(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz

    def is_point_inside(self, xx, yy, zz):
        left_side = (self.x - xx) ** 2 + (self.y - yy) ** 2 + (self.z - zz) ** 2
        if left_side <= self.r ** 2:
            return True
        return False

#Практичне завдання 7.2
"""Розробити класс Student для представлення відомостей про успішність слухача курсу Prometheus. Об'єкт класу має містити поля для збереження імені студента та балів, отриманих ним за виконання практичних завдань і фінального екзамена.

Забезпечити наступні методи класу:

конструктор, який приймає рядок -- ім'я студента -- та словник, що містить налаштування курсу у наступному форматі:
conf = {
'exam_max': 30, # кількість балів, доступна за здачу екзамена
'lab_max': 7, # кількість балів, доступна за виконання 1 практичної роботи
'lab_num': 10, # кількість практичних робіт в курсі
'k': 0.61, # частка балів від максимума, яку необхідно набрати для отримання сертифікату
}.
метод make_lab(m,n), який приймає 2 аргументи та повертає посилання на поточний об'єкт. Тут m -- кількість балів набрана за виконання завдання (ціле або дійсне число), а n -- ціле невід'ємне число, порядковий номер завдання (лаби нумеруються від 0 до lab_num-1). При повторній здачі завдання зараховується остання оцінка. Якщо n не задане, мається на увазі здача першого невиконаного практичного завдання. Врахувати, що під час тестування система іноді дає збої, тому за виконання завдання може бути нараховано більше балів ніж це можливо за правилами курсу, що не повинно впливати на рейтинг студента. Крім того в системі можуть міститися додаткові завдання, чиї номери виходять за межі 0..lab_num -- звичайно, бали за них не повинні зараховуватися для отримання сертифікату.
метод make_exam(m), який приймає 1 аргумент -- ціле або дійсне число, оцінку за фінальний екзамен, та повертає посилання на поточний об'єкт. Як і у випадку з практичними завданнями, оцінка за екзамен в результаті помилки іноді може перевищувати максимально допустиму.
метод is_certified(), який повертає тьюпл, що містить дійсне число (суму балів студента за проходження курсу), та логічне значення True або False в залежності від того, чи достатньо цих балів для отримання сертифікату.
Так як курс є доступним онлайн і не має дедлайнів на здачу робіт, студент може виконувати роботи в довільному порядку. Вважати, що кількість спроб на виконання кожного з завдань необмежена.

Приклад послідовності дій для тестування класу:
conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}
oleg = Student('Oleg', conf)
oleg.make_lab(1) \ # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
.make_lab(8,0) \ # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
.make_lab(1) \ # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
.make_lab(10,7) \ # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
.make_lab(4,1) \ # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
.make_lab(5) \ # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
.make_lab(6.5) \ # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print oleg.is_certified() # (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print oleg.is_certified() # (62.5, True)"""

class Student(object):

    def __init__(self, name, conf, labs = None, exam = None):
        self.name = name
        self.conf = conf
        self.labs = labs
        self.exam = exam
        keys = conf.keys()
        if 'exam_max' in keys:
            self.exam_max = conf['exam_max']
        if 'lab_max' in keys:
            self.lab_max = conf['lab_max']
        if 'lab_num' in keys:
            self.lab_num = conf['lab_num']
        if 'k' in keys:
            self.k = conf['k']
        self.labs = []
        self.exam = 0
        while len(self.labs) != self.lab_num:
            self.labs.append(0)


    def make_lab(self, m, n = None):
        if isinstance(m, (int, float)):
            
            if n != None:
                if (n+1) <= len(self.labs):
                    if m <= self.lab_max:
                        self.labs[n] = m
                    else:
                        self.labs[n] = self.lab_max
                else:
                    while ((n+1) != len(self.labs)):
                        self.labs.append(0)
                    if m <= self.lab_max:
                        self.labs[n] = m
                    else:
                        self.labs[n] = self.lab_max
            else:
                 if 0 in self.labs:
                    n = self.labs.index(0)
                    if m <= self.lab_max:
                        self.labs[n] = m
                    else:
                        self.labs[n] = self.lab_max
            return self
        return None

    def make_exam(self, m):
        if isinstance(m, (int, float)):
            if m <= self.exam_max and m > 0:
                self.exam = m
            else:
                self.exam = self.exam_max
            return self
        return None

    def is_certified(self):
        result_tuple = ()
        sum_marks = sum(self.labs[:self.lab_num]) + self.exam
        min_count_marks = (self.exam_max + self.lab_max * self.lab_num) * self.k
        if  sum_marks >= min_count_marks:
            result_tuple = (sum_marks, True)
        else:
            result_tuple = (sum_marks, False)
        return result_tuple

#Практичне завдання 7.3
"""Розробити класс SuperStr, який наслідує функціональність стандартного типу str і містить 2 нових методи:

метод is_repeatance(s), який приймає 1 аргумент s та повертає True або False в залежності від того, чи може бути поточний рядок бути отриманий цілою кількістю повторів рядка s. Повернути False, якщо s не є рядком. Вважати, що порожній рядок не містить повторів.
метод is_palindrom(), який повертає True або False в залежності від того, чи є рядок паліндромом. Регістрами символів нехтувати. Порожній рядок вважати паліндромом.
Приклад послідовності дій для тестування класу:
s = SuperStr('123123123123')
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False
print s.is_palindrom() # False
print s # 123123123123 (рядок)
print int(s) # 123123123123 (ціле число)
print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom() # True"""

from __future__ import division

class SuperStr(str):
    def __init__(self, sss):
        self.sss = sss

    def is_repeatance(self, s_part):
        if type(s_part) == type(self.sss):
            if len(s_part) != 0 and len(self.sss) != 0:
                if len(self.sss)/len(s_part) == self.sss.count(s_part):
                    return True
                else:
                    return False
            return False
        return False

    def is_palindrom(self):
        new_string = self.sss.lower()
        reverse_string = ''.join((list(new_string))[::-1])
        if new_string == reverse_string:
            return True
        else:
            return False

#Практичне завдання 7.4
"""Розробити функцію create_calendar_page(month,year), 
яка приймає 2 аргументи -- цілі числа -- місяць (нумерація починається з 1) і рік, 
та повертає оператором return 1 рядок, який містить сторінку календаря на цей місяць.

Якщо місяць та рік не задані, використати сьогоднішні значення.

Це значення є одним рядком із переносами рядка \n, пробіли після числа 28 відсутні. Зайві пробіли в кінці під-рядків або всього рядка, як і зайві порожні рядки недопустимі.

Тести із некорестними даними не проводяться.

Приклад викликів для тестування функції:
print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)"""

import calendar
from datetime import date, datetime


def create_calendar_page(month = None,year = None):
    if month == None:
        month = int(date.today().strftime('%m'))
    if year == None:
        year = int(date.today().strftime('%Y'))
    if isinstance(month, int) and month > 0:
        if isinstance(year, int):
            c = calendar.Calendar(0)
            s = ''
            for ls in c.monthdayscalendar(year, month):
                for n, i in enumerate(ls):
                    if i < 10:
                        ls[n] = '%02d'% ls[n]
                    if i == 0:
                        ls[n] = '  '
                s = s + str(' '.join(map(str, ls))).rstrip() + '\n'
            calendar_string = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
            return (calendar_string + s).rstrip() + ' \n'
        return None
    return None