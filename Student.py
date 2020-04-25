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

conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o1 = Student('Oleg', conf1)
print o1.is_certified()
o2 = Student('Oleg', conf1)
o2.make_lab(60).make_lab(35.2)
print o2.is_certified()
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print o3.is_certified()
o3.make_lab(20,1).make_lab(20,0)
print o3.is_certified()
o3.make_lab(50,2)
print o3.is_certified()
o3.make_lab(40,1)
print o3.is_certified()
conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}
o4 = Student('Oleg', conf2)
o4.make_exam(100)
print o4.is_certified()
o5 = Student('Oleg', conf2)
o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1)
print o5.is_certified()
o5.make_lab(7)
print o5.is_certified()
o5.make_exam(7)
conf3 = {'exam_max': 10,'lab_max': 1,'lab_num': 90,'k': 0.5,}
o6 = Student('Oleg', conf3)
for i in range(51): o6.make_lab(1)
print o6.is_certified()

