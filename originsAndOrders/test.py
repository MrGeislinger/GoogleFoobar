from test import *

print answer(1,31,99)
print answer(1,31,1)
print answer(1,1,99)

months = range(1,13)
days = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
yrs = range(1,100)


for m in months:
    for y in yrs:
        d = days[m]
        print "testing: ",(m,d,y)
        print answer(m,y,d)
        print answer(d,y,m)
        print answer(m,d,y)
        print answer(d,m,y)
        print answer(y,d,m)
        print answer(y,m,d)
