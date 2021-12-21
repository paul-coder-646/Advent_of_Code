import numpy as np

def parseInput(input):
    cinput = input.rstrip("\n")
    lines = cinput.split("\n")
    output = []
    for p in range(len(lines)):
        currentl = []
        currentr = []
        tmpresult = []
        tmpset = lines[p].split(" -> ")
        
        for c in range(2):
            if c == 0:
                tmpresult = tmpset[c].split(',')   
                currentl =[int(tmpresult[0]), int(tmpresult[1])]
            else:
                tmpresult = tmpset[c].split(',')   
                currentr =[int(tmpresult[0]), int(tmpresult[1])]
                
        output.append([currentl, currentr])
    return output


def computeMap(pairs):
    # determine matrix size needed
    max = 0
    for p in pairs:
        for c in range(2):
            for f in range(2):
                if p[c][f] > max:
                    max = p[c][f]
    
    # initialize array
    matrix = np.zeros([max+1, max+1], dtype=int)
    
    for p in pairs:
        
        xstart = p[0][0] 
        xstop = p[1][0]
        
        ystart = p[0][1] 
        ystop = p[1][1]
    
        if(xstart == xstop or ystart == ystop): # part1 
            if (xstart < xstop):
                for x in range (xstart, xstop+1):
                    matrix[ystart, x] += 1
                    
            elif (xstart > xstop):
                for x in range (xstart, xstop-1, -1):
                    matrix[ystart, x] += 1
            elif (ystart < ystop):
                for y in range (ystart, ystop+1):
                    matrix[y, xstart] += 1
            elif (ystart > ystop):
                for y in range (ystart, ystop-1, -1):
                    matrix[y, xstart] += 1
            else:
                print("Undefined")
        else: # part2
            if (xstart < xstop and ystart < ystop):
                for (y,x) in zip(range(ystart,ystop+1), range(xstart,xstop+1)):
                    matrix[y,x] += 1
            if (xstart > xstop and ystart < ystop):
                for (y,x) in zip(range(ystart,ystop+1), range(xstart,xstop-1,-1)):
                    matrix[y,x] += 1
                    
            if (xstart < xstop and ystart > ystop):
                for (y,x) in zip(range(ystart,ystop-1, -1), range(xstart,xstop+1)):
                    matrix[y,x] += 1
                    
            if (xstart > xstop and ystart > ystop):
                for (y,x) in zip(range(ystart,ystop-1, -1), range(xstart,xstop-1, -1)):
                    matrix[y,x] += 1
                
    return matrix 

def computeIntersec(matrix):
    counter = 0
    for m in matrix:
        for n in m:
            if n > 1:
                counter += 1
                
    return counter


def part1(matrix):
    result = computeIntersec(matrix)
    return result

def part2():
    result = computeIntersec(matrix)
    return result

if __name__ == '__main__':
    coordinates = parseInput(open('/Users/waverider/Desktop/Programming/Advent of Code/Day 5/input').read())
    matrix = computeMap(coordinates)
    print(f'The number of intersecting vents is ' + str(part2(matrix)))
    print(matrix)


