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

s1 = SuperStr('678678678678')
print s1.is_repeatance('6786')
print s1.is_repeatance('678')
print s1.is_repeatance('678678'),  '=', 'True'
print s1.is_repeatance('678678678'),  '=', 'False'
print s1.is_repeatance('q'),  '=', 'False'
print s1.is_repeatance(''),  '=', 'False'
print s1.is_repeatance(678),  '=', 'False'
print s1.is_repeatance([]),  '=', 'False'
print s1.is_repeatance([678]),  '=', 'False'
print s1.is_palindrom(),  '=', 'False'
print s1.isdigit(),  '=', 'True'
print int(s1),  '=', '678678678678'
print '("' + s1 + '")',  '=', '("678678678678")'
s2 = SuperStr('')
print s2.is_repeatance(''),  '=', 'False'
print s2.is_repeatance('a'),  '=', 'False'
print s2.is_palindrom(),  '=', 'True'
print bool(s2),  '=', 'False'
s3 = SuperStr('mystring1Gnirtsym')
print s3.is_repeatance('my'),  '=', 'False'
print s3.is_repeatance('q,.%;#'),  '=', 'False'
print s3.is_palindrom(),  '=', 'True'
print s3.lower(),  '=', 'mystring1gnirtsym'
print s3, '=', 'mystring1Gnirtsym'
s4 = SuperStr('q')
s4.is_repeatance(''),  '=', 'False'
print s4.is_repeatance('q'),  '=', 'True'
print s4.is_palindrom(),  '=', 'True'
print s4.upper(),  '=', 'Q'
