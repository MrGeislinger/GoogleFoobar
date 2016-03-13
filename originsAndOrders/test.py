from solution import *
from random import randint

# Testing specific dates
print answer(1,31,99) #01/31/99
print answer(1,31,1)  #01/31/01
print answer(1,1,99)  #01/01/99

# Create range of dates that are possible
months = range(1,13)
days = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
yrs = range(1,100)

# Test different combinations of dates from all month & year combinations
for m in months:
    for y in yrs:
	# Test day randomly within range of (1 - maxDayForMonth)
        d = randint(1,days[m])
        print "testing: ",(m,d,y)
        print answer(m,y,d)
        print answer(d,y,m)
        print answer(m,d,y)
        print answer(d,m,y)
        print answer(y,d,m)
        print answer(y,m,d)
