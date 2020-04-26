#Практичне завдання 5.1
"""Розробити функцію clean_list(list_to_clean), 
яка приймає 1 аргумент -- список будь-яких значень (рядків, цілих та дійсних чисел) довільної довжини, 
та повертає список, який складається з тих самих значень, але не містить повторів елементів. Це значить, що у випадку наявності значення в початковому списку в кількох екземплярах перший "екземпляр" значення залишається на своєму місці, а другий, третій та ін. видаляються.

Наприклад
Виклик функції: clean_list([1, 1.0, '1', -1, 1])
Повертає: [1, 1.0, '1', -1]
Виклик функції: clean_list(['qwe', 'reg', 'qwe', 'REG'])
Повертає: ['qwe', 'reg', 'REG']
Виклик функції: clean_list([32, 32.1, 32.0, -123])
Повертає: [32, 32.1, 32.0, -123]
Виклик функції: clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
Повертає: [1, 2, 3, 4, 5, 6, '2', 7, 8, 9, 0]"""

def clean_list(list_to_clean):
    new_string = []
    for i in list_to_clean:
        try:
            index_element = new_string.index(i)
        except ValueError:
            index_element = -1
        if index_element != -1:
            if type(new_string[index_element]) != (type(i)):
                new_string.append(i)
        else: new_string.append(i)
    return new_string

#Практичне завдання 5.2
"""Розробити функцію counter(a, b), 
яка приймає 2 аргументи -- цілі невід'ємні числа a та b, 
та повертає число -- кількість різних цифр числа b, які містяться у числі а.

Наприклад
Виклик функції: counter(12345, 567)
Повертає: 1
Виклик функції: counter(1233211, 12128)
Повертає: 2
Виклик функції: counter(123, 45)
Повертає: 0"""

def counter(a,b):

    a_list = list(str(a))
    b_list = list(str(b))
    new_b = []
    counte_r = 0

#remove the same elements in 'b'

    for i in b_list:
        try:
            index_element = new_b.index(i)
        except ValueError:
            index_element = -1
        if index_element == -1:
                new_b.append(i)

#find count of numbers of 'b' in 'a'

    for i in new_b:
        try:
            index_element = a_list.index(i)
        except ValueError:
            index_element = -1
        if index_element != -1:
            counte_r = counte_r + 1
    return counte_r

#Практичне завдання 5.3
"""Розробити функцію super_fibonacci(n, m), 
яка приймає 2 аргументи -- додатні цілі числа n та m (0 < n, m <= 35), 
та повертає число -- n-й елемент послідовності супер-Фібоначчі порядку m.

Нагадуємо, що послідовність Фібоначчі -- це послідовність чисел, в якій кожний елемент дорівнює сумі двох попередніх. Послідовністю супер-Фібоначчі порядку m будемо вважати таку послідовність чисел, в якій кожний елемент дорівнює сумі m попередніх. Перші m елементів (з порядковими номерами від 1 до m) вважатимемо одиницями.

Наприклад
Виклик функції: super_fibonacci(2, 1)
Повертає: 1
Виклик функції: super_fibonacci(3, 5)
Повертає: 1
Виклик функції: super_fibonacci(8, 2)
Повертає: 21
Виклик функції: super_fibonacci(9, 3)
Повертає: 57"""

def super_fibonacci(n,m):
    s = []
    count = 0
    for i in range(m):
        i = 1
        s.append(i)
        count = count + 1
    while len(s) < n:
        s.append(sum(s[(count-m):]))
        count = count + 1
    return s[-1]

#Практичне завдання 5.4
"""Розробити функцію file_search(folder, filename), 
яка приймає 2 аргументи -- список folder та рядок filename, 
та повертає рядок -- повний шлях до файлу або папки filename в структурі folder.

Файлова структура folder задається наступним чином:

Список -- це папка з файлами, його 0-й елемент містить назву папки, а всі інші можуть представляти або файли в цій папці (1 файл = 1 рядок-елемент списку), або вкладені папки, які так само представляються списками. Як і в файловій системі вашого комп'ютера, шлях до файлу складається з імен всіх папок, в яких він міститься, в порядку вкладеності (починаючи з зовнішньої і до папки, в якій безпосередньо знаходиться файл), розділених "/".

Вважати, що імена всіх файлів є унікальними. Повернути логічне значення False, якщо файл не знайдено.

Наприклад
Виклик функції: file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
Повертає: 'C:/ideas.txt'
Виклик функції: file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
Повертає: False
Виклик функції: file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
Повертає: '/home/user2/desktop/new folder/hereiam.py'

Лапки не повертаються і використані тут для розрізнення логічного False та рядків."""

def file_search(folder, filename):
    if len(folder) == 1:
        return False
    path = str(folder[0]) + '/'
    if filename in folder[1:]:
        return path + filename
    else:
        for item in folder[1:]:
            if type(item) is list and len(item)> 1:
                src = file_search(item, filename)
                path = path + str(src)
                return path
            path = ''
            return False