import random


def make_sudoku(size):
    if isinstance(size, int) and size >= 1 and size <= 42:
        list_result = []
        max_size = size**2
        l = list(xrange(1, max_size+1))
        # h - count of squares
        for h in range(size):
            # i - each line in the square
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


print make_sudoku(1)
