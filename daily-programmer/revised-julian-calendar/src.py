#brute force emthod of calculating # of leap years 

def divis_by_4(year):
    return year % 4 == 0
 

def divis_by_100(year):
    return year % 100 == 0
   
def remain_by_900(year):
    return year % 900 == 200 or year % 900 == 600


def is_leap_year(year):
    return (divis_by_4(year)) and not ((divis_by_100(year)) and (not remain_by_900(year)))


def leaps(start, end):
    i = 0
    while start < end:
        if is_leap_year(start):
            i += 1
        start += 1
    return(i)

print(leaps(123456, 7891011))
