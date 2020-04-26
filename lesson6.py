#Практичне завдання 6.1
"""Розробити функцію count_holes(n), 
яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число, 
та повертає ціле число -- кількість "отворів" у десятковому записі цього числа друкованими цифрами (вважати, що у "4" та у "0" по одному отвору), або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: є дійсним або взагалі не числом.

Незначущими нулями на початку запису числа, якщо такі є, нехтувати.

Наприклад
Виклик функціїі: count_holes('123')
Повертає: 0
Виклик функціїі: count_holes(906)
Повертає: 3
Виклик функціїі: count_holes('001')
Повертає: 0
Виклик функціїі: count_holes(-8)
Повертає: 2
Виклик функціїі: count_holes(-8.0)
Повертає: ERROR"""

def count_holes(n):
    holes_in_numbers = {9: 1, 8: 2, 7: 0, 6: 1, 5: 0, 4: 1, 3: 0, 2: 0, 1: 0, 0: 1}
    count = 0
    error = 'ERROR'
    
    if type(n) is float:
        return error
    if type(n) is list:
        return error
    if n == None:
        return error
    if isinstance(n, long) or isinstance(n, str) or isinstance(n, int):
        k = str(n)
        if k.lstrip('-').isdigit() == True:
            k = str(abs(int(n)))
            for i in k:
                count = count + holes_in_numbers.get(int(i), 'Nothing found')
            return count
        else:
            return error

#Практичне завдання 6.2
"""Розробити функцію encode_morze(text), 
яка приймає 1 аргумент -- рядок, 
та повертає рядок, який містить діаграму сигналу, що відповідає переданому тексту, 
закодованому міжнародним кодом Морзе для англійського алфавіту. Розділові та інші знаки, 
що не входять до латинського алфавіту, ігнорувати. Регістром літер нехтувати.

Для передачі повідомлення за одиницю часу приймається тривалість однієї крапки. 
Тривалість тире дорівнює трьом крапкам. Пауза між елементами одного знака -- одна крапка, 
між знаками в слові -- 3 крапки, між словами -- 7 крапок. Словом вважати послідовність 
символів, обмежена пробілами. Результуюча "діаграма" демонструє наявність сигналу в кожний 
проміжок часу: на і-й позиції знаходиться "^", якщо в цей момент передається сигнал, і "_", якщо 
сигналу немає. Зайві паузи в кінці повідомлення на "діаграмі" відсутні.

Наприклад
Виклик функції: encode_morze('Morze code')
Повертає: ^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^
Виклик функції: encode_morze('Prometheus')
Повертає: ^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^
Виклик функції: encode_morze('SOS')
Повертає: ^_^_^___^^^_^^^_^^^___^_^_^
Виклик функції: encode_morze('1')
Повертає: """

import re
def encode_morze(text):
    morse_code = {"A" : ".-","B" : "-...","C" : "-.-.","D" : "-..","E" : ".", "F" : "..-.","G" : "--.","H" : "....","I" : "..","J" : ".---","K" : "-.-","L" : ".-..","M" : "--","N" : "-.","O" : "---","P" : ".--.","Q" : "--.-","R" : ".-.","S" : "...","T" : "-","U" : "..-", "V" : "...-","W" : ".--","X" : "-..-","Y" : "-.--","Z" : "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}
    radio_sygnal = {"-": "^^^", ".": "^", "1": "_", "3": "___", "7": "_______"}
    sygnal = ''
    text = re.sub(r'[^a-zA-Z ]',r'',text)
    if isinstance(text, str):
        for letter in text:
            if letter != ' ':
                code_of_letter = morse_code.get(str(letter.upper()), 'Nothing found')
                for symbol in code_of_letter:
                    sygnal = sygnal + radio_sygnal.get(str(symbol), 'Nothing found') + radio_sygnal.get('1', 'Nothing found')
                sygnal = sygnal[:-1]
                sygnal = sygnal + radio_sygnal.get("3")
            else:
                sygnal = sygnal[:-3]
                sygnal = sygnal + radio_sygnal.get("7")
        sygnal = sygnal[:-3]
        return sygnal

#Практичне завдання 6.3
"""Розробити функцію saddle_point(matrix), 
яка приймає 1 аргумент -- прямокутну матрицю цілих чисел, задану у вигляді списка списків, 
та повертає тьюпл із координатами "сідлової точки" переданої матриці або логічну константу False, якщо такої точки не існує.

Сідловою точкою вважається такий елемент матриці, який є мінімальним (строго менше за інші) у своєму рядку та максимальним (строго більше за інші) у своєму стовпці, наприклад:
матриця:
1 2 3
0 2 1
"1" в лівому верхньому кутку (за координатами (0;0)) є сідловою точкою матриці.

Вважати, що передані дані є коректними, тобто матриця не містить інших значень крім цілих чисел, а всі вкладені списки мають однакову довжину. Результуючий тьюпл містить два числа -- порядкові номери сідлової точки в рядку (індекс його списка у зовнішньому списку) та в стовпці (індекс у внутрішньому списку).

Наприклад
1 2 3
3 2 1
Виклик функції: saddle_point([[1,2,3],[3,2,1]])
Повертає: False
8 3 0 1 2 3 4 8 1 2 3
3 2 1 2 3 9 4 7 9 2 3
7 6 0 1 3 5 2 3 4 1 1
Виклик функції: saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])
Повертає: (1, 2)
21
Виклик функції: saddle_point([[21]])
Повертає: (0, 0)"""

def saddle_point(matrix):
    s_point = ()
    flag = False
    if isinstance(matrix, list):
        for i in matrix:
            s = []
            minimum = min(i)
            ind = i.index(minimum)
            for row in matrix:
                s.append(row[ind])
            if minimum in s:
                s.remove(minimum)
            if not s:
                s_point = (matrix.index(i),ind)
            else:
                if minimum > max(s) and i.count(minimum) == 1:
                    s_point = (matrix.index(i),ind)
        if s_point == ():
            return flag
        else:
            return s_point

#Практичне завдання 6.4
"""Розробити функцію find_most_frequent(text), 
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.

Наприклад
Виклик функції: find_most_frequent('Hello,Hello, my dear!')
Повертає: ['hello']
Виклик функції: find_most_frequent('to understand recursion you need first to understand recursion...')
Повертає: ['recursion', 'to', 'understand']
Виклик функції: find_most_frequent('Mom! Mom! Are you sleeping?!!!')
Повертає: ['mom']"""

def find_most_frequent(text):
    list_of_words =[]
    word = ''
    result = []
    if isinstance(text, str):
        new_text = text + ' '
        for letter in new_text:
            if letter.isalpha():
                word = word + letter.lower()
                if text.index(letter) == -1:
                    list_of_words.append(word)
            else:
                if word != '':
                    list_of_words.append(word)
                    word = ''
        count_words = {i: list_of_words.count(i) for i in list_of_words}
        if bool(count_words) != False:
            maximum_element = max(count_words.values())
            for key, value in count_words.items():
                if value == maximum_element:
                    result.append(key)
            return sorted(result)
        else:
            return list_of_words