# Question 5: Check whether a year is a leap year.

year = 1900
if(year%4 == 0) or (year%100 != 0 and year%4 == 0) :
    print("year is leap year")
else:
    print("year is not leap year")    