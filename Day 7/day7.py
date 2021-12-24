import math

def parseInput(crabinput):
    crabinput = crabinput.split(',')
    crabinput = [int(a) for a in crabinput]
    return crabinput

def calculateFuel(crablist): # part 1
    totalminfuel = math.inf
    maxcrabpos = 0
    minindex = 0

    # determine how long the array shall be
    for c in crablist:
        if c > maxcrabpos:
            maxcrabpos = c

    values = [0] * maxcrabpos

    # for every possible value all crabs could travel to, calculate the TTC (TotalTravelCost)
    # of all crabs
    for i in range(len(values)):
        for e in crablist:
            values[i] += int(((abs(e - i))*(abs(e - i) + 1))/2)

    for i in enumerate(values):
        if i[1] < totalminfuel:
            totalminfuel = i[1]
            minindex = i[0]

    minstartcrab = crablist[minindex]

    #return minfuel, endposition
    return maxcrabpos, totalminfuel, minstartcrab


if __name__ == '__main__':
    input = parseInput(open('/Users/waverider/Desktop/Programming/Advent of Code/Day 7/input').read())
    print(calculateFuel(input))

