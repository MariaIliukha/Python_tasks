#Практичне завдання №2.1
"""Вхідні дані: 3 дійсних числа -- аргументи командного рядка.

Вихідні дані: результат обчислення формули


Аргументи передаються в порядку, зазначеному у формулі, назви змінних можуть використовуватися будь-які.

Приклад
Вхідні дані: 1 1 0.25
Приклад виклику: python lab2_1.py 1 1 0.25
Результат: 1.59576912161"""

import sys, math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

f = (1/(c*math.sqrt(2*math.pi)))*math.exp(((-(a-b)**2))/(2*math.pow(c,2)))
print f

#Практичне завдання №2.2
Вхідні дані: 3 числа x, y та z. x, y -- невід'ємні цілі числа, z дорівнює 0 або 1. x не дорівнює 0. Передаються як аргументи командного рядка.

Вихідні дані: рядок "Everybody sing a song: <текст пісеньки>.", де <текст пісеньки> формується з у куплетів, розділених пробілами. Всі куплети однакові і складаються з x 'la' через дефіс. Якщо z дорівнює одиниці, в кінці ставиться окличний знак, інакше крапка. За відсутності куплетів пробіл перед крапкою/окличним знаком не ставиться.

Підказка: для цього можна застосувати множення рядків.

Приклад
Вхідні дані: 2 3 1
Приклад виклику: python lab2_2.py 2 3 1
Результат: Everybody sing a song: la-la la-la la-la!
Вхідні дані: 1 0 0
Приклад виклику: python lab2_2.py 1 0 0
Результат: Everybody sing a song:."""

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

if z==1 and x!=0: print('Everybody sing a song:'+ y*(' '+((x-1)*('la-'))+'la')+ '!')
if z==0 and x!=0: print('Everybody sing a song:'+ y*(' '+((x-1)*('la-'))+'la')+ '.')

