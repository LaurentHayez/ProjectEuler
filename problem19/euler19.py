import calendar

cal = calendar.Calendar(6)

sum = 0
for year in range(1901, 2001):
    for month in range(1,13):
        if (1,6) in cal.monthdays2calendar(year,month)[0]:
            sum += 1

print(sum)
