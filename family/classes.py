from datetime import datetime, timedelta

class Friend(object):
    name = None
    birthday = None
    mobile = None
    fb = None
    email = None

    def __init__(self, dic = None):
        keys = dic.keys()
        if 'name' in keys:
            self.name = dic['name']
        if 'birthday' in keys:
            self.birthday = datetime.strptime(dic['birthday'], '%d/%m/%y')
        if 'mobile' in keys:
            self.mobile = dic['mobile']
        if 'fb' in keys:
            self.fb = dic['fb']
        if 'email' in keys:
            self.email = dic['email']

    def how_to_contact(self):
        if self.fb:
            return 'Write in FaceBook: ' + str(self.fb)
        elif self.mobile:
            return 'Call: ' + str(self.mobile)
        elif self.email:
            return 'Write email: ' + str(self.email)
        return 'But how to greet'

    def days_to_birthday(self):
        if isinstance(self.birthday, datetime):
            today = datetime.now()
            next_birthday = self.birthday.replace(year = today.year)
            if next_birthday < today:
                next_birthday = self.birthday.replace(year = today.year + 1)
            return (next_birthday - today).days
        return None

class FindList(object):
    family = []

    def __init__(self, my_family):
        for record in my_family:
            self.family.append(Friend(record))

    def get_closest_birthday(self):
        if not len(self.family):
            return 'This list is empty'
        closest = (365, self.family[0])
        for person_of_family in self.family:
            days_left = person_of_family.days_to_birthday()
            if days_left < closest[0]:
                closest = (days_left, person_of_family)
        return 'The next birthday is in %s days (%s) -- %s' % (closest[0], closest[1].name, closest[1].how_to_contact())
