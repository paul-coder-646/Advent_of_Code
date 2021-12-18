

def count_depth():
    depthcounter = 0
    lines = []

    with open('/Users/waverider/Desktop/Programming/Advent of Code/Day 1/input') as i:
        lines = i.readlines()
    lines = [line.rstrip() for line in lines]
        
    for index in range(len(lines)):
        if ( int(lines[index]) + int(lines[index -1]) + int(lines[index -2]) ) > ( int(lines[index - 1]) + int(lines[index -2]) + int(lines[index - 3]) ):
            depthcounter += 1
            
    print(f'the depth of the vessel is ' + str(depthcounter)) 
    
count_depth()