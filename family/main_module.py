from family.classes import FindList
from family.data import my_family as data

f1 = FindList(data)
print f1.get_closest_birthday()
