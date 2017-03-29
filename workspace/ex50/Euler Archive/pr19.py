# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
day_names = {'0':'Monday','1':'Tuesday','2':'Wednesday','3':'Thursday','4':'Friday','5':'Saturday','6':'Sunday'};
month_names = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'};
month_days = [31,28,31,30,31,30,31,31,30,31,30,31];
days = range(0,7);
year = 1900;
year_length = 365;
months = range(1,13);
leap_count = 0;
month = 1;
date = 0;
d = 0;
count = 0;

def get_month_and_date(n,m): # n as date out of 365/366, m as leap_count
    month = 1;
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31];
    if m == 4:
        month_days[1] += 1;
    for i in range(13):
        if not (n + 1) > sum(month_days[:i]):
            month = i;
            date = n - sum(month_days[:i-1]) + 1;
            break
        elif n == 365:
            date = 31;
    return date, month_names.get(str(month));



for n in range(365*101+25):
    if d == year_length:
        year += 1;
        leap_count += 1;
        if leap_count < 4:
            year_length = 365;
        elif leap_count > 4:
            leap_count = 1;
            year_length = 365;
        else:
            year_length = 366
        d = 0
    # print n,d, day_names.get(str(n % 7)), get_month_and_date(d,leap_count), year, leap_count;
    if get_month_and_date(d,leap_count)[0] == 1 and day_names.get(str(n % 7)) == 'Sunday':
        count += 1;
        # print n, day_names.get(str(n % 7)), get_month_and_date(d,leap_count), year;
    d += 1;

print count - 1; # there were 2 sundays on the first of the month in 1900