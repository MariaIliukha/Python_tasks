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
            return result_list_of_pairs, len(result_list_of_pairs)

        return None


s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(2)
