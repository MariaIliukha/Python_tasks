#Практичне завдання №4.1
"""Вхідні дані: рядок, передається в програму як аргумент командного рядка. Може містити пробіли, літери латинського алфавіту в будь-якому регістрі та цифри. Для передачі одним значенням рядок, що містить пробіли, береться в подвійні лапки.

Результат роботи: рядок "YES", якщо отриманий рядок є паліндромом, або "NO" - якщо ні. Рядок вважається паліндромом, якщо він однаково читається як зліва направо, так і справа наліво. Відмінністю регістрів та пробілами знехтувати.

Наприклад
Вхідні дані: 0
Приклад виклику: python lab4_1.py 0
Результат: YES
Вхідні дані: puppy
Приклад виклику: python lab4_1.py puppy
Результат: NO
Вхідні дані: "mystring1Gni rts ym"
Приклад виклику: python lab4_1.py "mystring1Gni rts ym"
Результат: YES"""

import sys

text = sys.argv[1]

new_text = ''

for letter in text:
    if (letter != ' '):
        new_text = new_text + letter.lower()
# print new_text
if (new_text[::] == new_text[::-1]):
    print 'Yes'
else:
    print 'No'

#Практичне завдання №4.2
"""Вхідні дані: довільна, відмінна від нуля, кількість значень - аргументів командного рядка. Значеннями-аргументами можуть бути числа або рядки, які складаються з цифр та літер латинського алфавіту без пробілів.

Результат роботи: рядок, що складається з отриманих значень в зворотньому порядку, записаних через пробіл. Пробіл в кінці рядка відсутній.

Наприклад
Вхідні дані: 1
Приклад виклику: python lab4_3.py 1
Результат: 1
Вхідні дані: qwe asd zxc 123
Приклад виклику: python lab4_3.py qwe asd zxc 123
Результат: 123 zxc asd qwe
Вхідні дані: padawan young my HAVE MUST YOU PATIENCE
Приклад виклику: python lab4_3.py padawan young my HAVE MUST YOU PATIENCE
Результат: PATIENCE YOU MUST HAVE my young padawan"""

import sys
#x = sys.argv[1:]
#print x[::-1]

x = sys.argv[1:]
x.reverse()
i = 0
reverse_text = ''

while i < len(x):
    reverse_text = reverse_text + x[i] + ' '
    i = i + 1
print reverse_text.rstrip()


#Практичне завдання №4.3
"""Вхідні дані: рядок, що складається з відкриваючих та закриваючих круглих дужок - аргумент командного рядка. Для передачі в якості рядка послідовність береться в подвійні лапки.

Результат роботи: рядок "YES", якщо вхідний рядок містить правильну дужкову послідовність; або рядок "NO", якщо послідовність є неправильною. Дужкова послідовність вважається правильною, якщо всі дужки можна розбити попарно "відкриваюча"-"закриваюча", при чому в кожній парі закриваюча дужка слідує після відкриваючої.

Пояснення для математиків:
"" (порожній рядок) - правильна дужкова послідовність (ПДП)
"(ПДП)" - також ПДП
"ПДППДП" (дві ПДП записані поряд) - також ПДП

Наприклад
Вхідні дані: ")("
Приклад виклику: python lab4_3.py ")("
Результат: NO
Вхідні дані: "(()(()"
Приклад виклику: python lab4_3.py "(()(()"
Результат: NO
Вхідні дані: "(()(()()))"
Приклад виклику: python lab4_3.py "(()(()()))"
Результат: YES
Вхідні дані: "())()(()())(()"
Приклад виклику: python lab4_3.py "())()(()())(()"
Результат: NO"""

import sys

text = sys.argv[1]

left = 0
right = 0
i = 0
flag = True

while i < len(text):
    if text[i] == '(':
        left = left + 1
    if text[i] == ')':
        right = right + 1
        if right > left:
            flag = False
    i = i + 1
if flag == True and right == left:
    print 'Yes'
else:
    print 'No'

#Практичне завдання №4.4
"""Завдання передбачає пошук "щасливих" квитків. "Щасливим" називається такий тролейбусний квиток, в якому сума перших трьох цифр дорівнює сумі останніх трьох. Наприклад 030111 (0+3+0 = 1+1+1), 902326 (9+0+2 = 3+2+6), 001100 (0+0+1 = 1+0+0).

Вхідні дані: два цілих невід'ємних числа (0<=a1<=a2<=999999) - аргументи командного рядка.

Результат роботи: кількість "щасливих квитків", чиї номери лежать на проміжку від a1 до a2 включно. Якщо число на проміжку має менше 6 розрядів, вважати, що на його початку дописуються нулі у необхідній кількості, як це і відбувається при нумерації квитків. Виводити номери квитків не треба.

Наприклад
Вхідні дані: 0 1000
Приклад виклику: python lab4_4.py 0 1000
Результат: 1
Пояснення: номер 000000
Вхідні дані: 1001 1122
Приклад виклику: python lab4_4.py 1001 1122
Результат: 3
Пояснення: номери 001001, 001010, 001100
Вхідні дані: 222222 222333
Приклад виклику: python lab4_4.py 222222 222333
Результат: 7
Пояснення: номери 222222, 222231, 222240, 222303, 222312, 222321, 222330"""

import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
a = int
lucky_ticket = 0

if 0<=a1<=a2 and a1<=a2<=999999:
    for a in range(a1, a2+1):
        a = list(str(a))
        a.reverse()
        while len(a) < 6:
            a.append(0)
        a.reverse()
        sum1 = int(a[0])+int(a[1])+int(a[2])
        sum2 = int(a[3])+int(a[4])+int(a[5])
        if  sum1 == sum2:
            lucky_ticket = lucky_ticket + 1
    print lucky_ticket
else:
    print 'Impossible'




