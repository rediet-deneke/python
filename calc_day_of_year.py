def is_year_leap(year):
    return year % 4 == 0


def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month == 1:
        return 31
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31

def day_of_year(year, month, day):
    days = 0
    for i in range(month):
        ret = days_in_month(year, i + 1)
        #current month
        if i == month:
            days += ret - (ret - day)
        else:
            days += ret
        
    return days

print(day_of_year(2024, 3, 7))
#print(day_of_year(2000, 2, 29))
