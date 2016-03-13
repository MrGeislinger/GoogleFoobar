def isValidMonthDay(n1,n2):
    # Month/Day definitions
    months = range(1,13)
    days_dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    # Does the month match for first number?
    if( (n1 in months) and ( n2 <= days_dict[n1]) ):
        return True
    else:
        return False


def answer(x, y, z):
    # Change single digits to double strings
    singleDigits = [(oneD,"0%d" %oneD) for oneD in range(1,10)]
    doubleDigits = [(digit, "%d" %digit) for digit in range(10,100) ]
    numStrs  = dict( singleDigits + doubleDigits )

    # Find all combinations of month & days (can switch manually)
    # Note the third number in tuple is always year
    monthDayPairs = [ (x,y,z), (x,z,y), (y,z,x)]
    # Can ignore year since it is always valid
    numPossible = 0
    # Save temp months and days (don't repeat the same test)
    tempDay = 0
    tempMonth = 0
    tempYear = 0
    for n1,n2,n3 in monthDayPairs:
        # Since more than 1 date possible, stop here
        if(numPossible > 1):
            return "Ambiguous"
        # Test first pair
        if(isValidMonthDay(n1,n2) and (tempDay != n2) and (tempMonth != n1) ):
            numPossible += 1
            tempDay = n2
            tempMonth = n1
            tempYear = n3
        # Test backwards pair
        if(isValidMonthDay(n2,n1) and (tempDay != n1) and (tempMonth != n2) ):
            numPossible += 1
            tempDay = n1
            tempMonth = n2
            tempYear = n3
    # Above is passed if first match, so write string
    day_str  = numStrs[tempDay]
    mnth_str = numStrs[tempMonth]
    yr_str   = numStrs[tempYear]


    # Since hasn't returned yet, assume only one date was correct
    return "%s/%s/%s" %(mnth_str,day_str,yr_str)
