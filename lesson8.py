#Практичне завдання 8.1
"""Розробити класс CombStr для представлення рядка символів.

Забезпечити наступні методи класу:

конструктор, який приймає 1 аргумент -- рядок string.
метод count_substrings(length), який приймає 1 аргумент -- невід'ємне ціле число length, та повертає ціле число -- кількість всіх різних підрядків довжиною length, що містяться в рядку string.
Тести із некоректними даними не проводяться.

Послідовність символів substring вважається підрядком рядка string, якщо її можна отримати зі string шляхом відкидання символів з початку та/або з кінця рядка. Наприклад 'asd' є підрядком 'asdfg', а 'fgh' -- ні. Вважати, що порожніх підрядків не буває, тому для length=0 повертати 0.

Приклад послідовності дій для тестування класу:
s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0"""

class CombStr():
    def __init__(self, string):
        self.s_string = string

    def count_substrings(self, length=None):
        if length == 0:
            return 0
        if length == None:
            return None
        if isinstance(length, int) and length > 0:
            result_list_of_pairs = []
            sp = ''
            llist = []

            for indeex, i in enumerate(self.s_string):
                llist = []
                for j in self.s_string[indeex:indeex+length]:
                    llist.append(j)
                sp = ''.join(llist)
                if len(sp) == length:
                    if result_list_of_pairs.count(sp) == 0:
                        result_list_of_pairs.append(sp)
            llist = []
            if len(result_list_of_pairs) == 0:
                return 0
            for i in self.s_string[-length:]:
                llist.append(i)
            sp = ''.join(llist)
            if result_list_of_pairs.count(sp) == 0:
                result_list_of_pairs.append(sp)
            return len(result_list_of_pairs)

        return None

#Практичне завдання 8.4
"""Розробити функцію make_sudoku(size), 
яка приймає 1 аргумент -- додатнє ціле число (1 <= size <= 42), 
та повертає список списків -- квадратну матрицю, що представляє судоку розмірності size.

Судоку розмірності X являє собою квадратну матрицю розмірністю X**2 на X**2, 
розбиту на X**2 квадратів розмірністю X на X, заповнену цілими числами таким чином, 
щоб кожна вертикаль, кожна горизонталь та кожний квадрат містили всі числа від 1 
до X**2 включно без повторів.
квадрат 9х9 (3**2 = 9), який складається з 9 квадратів 3х3. В кожній вертикалі розміщені різні числа від 1 до 9. Те саме стосується кожної горизонталі та кожного внутрішнього квадрату.

Дане завдання не має єдиного вірного розв'язку -- ваша функція повинна повертати результат, який задовольняє умові, за відведений час.

Тести із некоректними даними не проводяться

Приклад вхідних і вихідних даних:
print make_sudoku(1) # [[1]]
print make_sudoku(2) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]
print make_sudoku(3) # [[3,5,8,1,2,7,6,4,9],[6,7,4,5,8,9,3,2,1],[2,1,9,3,4,6,5,7,8],[9,8,6,7,1,4,2,5,3],[4,3,1,2,6,5,8,9,7],[7,2,5,9,3,8,1,6,4],[1,6,3,4,7,2,9,8,5],[8,9,7,6,5,1,4,3,2],[5,4,2,8,9,3,7,1,6]]"""

import random


def make_sudoku(size):
    if isinstance(size, int) and size >= 1 and size <= 42:
        list_result = []
        max_size = size**2
        l = list(xrange(1, max_size+1))
        for h in range(size):
            for i in range(size):
                list_result.append(l)
                lll = []
                for j in l[size:]:
                    lll.append(j)
                for k in l[:size]:
                    lll.append(k)
                l = lll
            sp = []
            n = 0
            for i in l[(n+1):]:
                sp.append(i)
            for j in l[:(n+1)]:
                sp.append(j)
            l = sp
            n = n + 1
        return list_result
    return None