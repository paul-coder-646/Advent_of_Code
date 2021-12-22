
def parseInput(input, efficient=True):
    if efficient:
        counter = [0,0,0,0,0,0,0,0,0,0]
        fishlist = input.split(',')
        fishlist = [int(a) for a in fishlist if a != 0]
        
        for j in fishlist:
            counter[j] += 1
            
        return counter
            
    
    else:
        fishlist = input.split(',')
        fishlist = [int(a) for a in fishlist if a != 0]
        firsttime = [False] * len(fishlist)
        fishchart = (fishlist, firsttime)
        return fishchart


def lifecycle_naive(fishlist): #part1
    counter = 0
    #phase 1 find any fish that are ready to reproduce
    for j in range(len(fishlist[0])):
        if fishlist[0][j] == 0:
            fishlist[0][j] = 7
            counter += 1
    for i in range(counter):
        fishlist[0].append(8)
        fishlist[1].append(True) # new kid fishie
    
    #phase 2 all fishies are 1 step closer to being pregnant
    for n in range(len(fishlist[0])):
        if fishlist[1][n] is True:
            fishlist[1][n] = False
        else:
            fishlist[0][n] -= 1
            
    return fishlist

def lifecycle_faster(counter):
    counter[7] += counter[0]
    counter[9] += counter[0]
    counter[0] -= counter[0]
        
    for i in range(len(counter)):
        counter[i-1] += counter[i]
        counter[i] -= counter[i]
    
    return counter


if __name__ == '__main__':
    fishcounter =(parseInput(open('/Users/waverider/Desktop/Programming/Advent of Code/Day 6/input').read(), True))
    
    print(f'Initially, there are {sum(fishcounter)} fishies:')
    
    for i in range(1,257):
        fishcounter = lifecycle_faster(fishcounter)
        print(f'On Day {i} there are {sum(fishcounter)} fishies')
    print(fishcounter)
    