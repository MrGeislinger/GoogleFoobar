# (better way? -> max list length is 10^3)
def tempAnswer(x):
    # Notice that if the weight (x) is greater than the sum of all
    # 3^n set of weights, then the 3^(n+1) weight must be used
    sumOfPowers = 1
    largestPower = 0
    while(x > sumOfPowers):
        # Add to sum and then keep track of power
        largestPower += 1
        sumOfPowers += pow(3,largestPower)

    # Switch 'L' <-> 'R'
    switchDict = {'L':'R', 'R':'L', '-':'-'}

    # Last power is always on the right side
    # Take from next highest power, and check which has more
    left = x
    right = pow(3,largestPower)
    # Recursively find power?
    if(left == 1):
        return [(largestPower,"R")]
    elif(left == 0):
        return [(largestPower,"-")]
    else:
        # Find difference and find answer list to that
        diff = right - left
        if( diff > 0 ): # left < right
            # Change to dictionary after switching values
            tempAns = dict([(p,switchDict[l]) for p,l in tempAnswer(diff)])
            finalAns = []
            # Fill out the powers found and not used
            for p in range(largestPower):
                if p in tempAns:
                    finalAns += [(p,tempAns[p])]
                else:
                    finalAns += [(p,'-')]
            return finalAns + [(largestPower,'R')]
        else: # right < left
            # Need to swap the signs and make dictionary
            tempAns = dict(tempAnswer(diff*-1))
            finalAns = []
            # Fill out the powers found and not used
            for p in range(largestPower):
                if p in tempAns:
                    finalAns += [(p,tempAns[p])]
                else:
                    finalAns += [(p,'-')]
            return  finalAns + [(largestPower,'R')]

def answer(x):
    return [w for (_,w) in tempAnswer(x)]
