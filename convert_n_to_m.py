def convert_n_to_m(x, n, m):
    system_number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15',
               'G': '16', 'H': '17', 'I': '18', 'J': '19', 'K': '20', 'L': '21', 'M': '22',
               'N': '23', 'O': '24', 'P': '25', 'Q': '26', 'R': '27', 'S': '28',
               'T': '29', 'U': '30', 'V': '31', 'W': '32', 'X': '33', 'Y': '34',
               'Z': '35'}
    list_x = []
    sum_inside_x = 0
    if isinstance(x, int) or isinstance(x, long) or isinstance(x, str) and isinstance(n, int) and\
            isinstance(m, int) and (1 <= n <= 36) and (1 <= m <= 36):
        for i in str(x):
            if i.upper() not in (system_number[:n]):
                return False
        # if value is 0
        if x == 0 or x == '0':
            return '0'
        # convert x to 10 number system
        for i in str(x):
            list_x.append(i)
        list_x.reverse()
        for y, i in enumerate(list_x):
            if i.upper() in system_number[10:]:
                i = letters[i.upper()]
            part_x = (int(i) * ((n)**y))
            sum_inside_x = sum_inside_x + part_x
        # convert sum_inside_x to m number system
        if m == 1:
            len_from_m = []
            while len(len_from_m) != sum_inside_x:
                len_from_m.append('0')
            return ''.join(len_from_m)
        else:
            result_m = []
            while (sum_inside_x / m) != 0:
                y = sum_inside_x % m
                if y > 9:
                    for k, v in letters.items():
                        if v == str(y):
                            y = k
                result_m.append(str(y))
                sum_inside_x = sum_inside_x / m
            last_number = sum_inside_x % m
            if last_number > 9:
                for k, v in letters.items():
                    if v == str(last_number):
                        last_number = k
            result_m.append(str(last_number))
            result_m.reverse()
            return ''.join(result_m)
    return False


print convert_n_to_m('aAA22', 11, 2)
