

import calendar
from datetime import date, datetime


def create_calendar_page(month = None,year = None):
    if month == None:
        month = int(date.today().strftime('%m'))
    if year == None:
        year = int(date.today().strftime('%Y'))
    if isinstance(month, int) and month > 0:
        if isinstance(year, int):
            c = calendar.Calendar(0)
            s = ''
            for ls in c.monthdayscalendar(year, month):
                for n, i in enumerate(ls):
                    if i < 10:
                        ls[n] = '%02d'% ls[n]
                    if i == 0:
                        ls[n] = '  '
                s = s + str(' '.join(map(str, ls))).rstrip() + '\n'
            calendar_string = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
            return (calendar_string + s).rstrip()
        return None
    return None

print create_calendar_page()


