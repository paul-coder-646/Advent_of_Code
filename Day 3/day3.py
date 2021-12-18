


with open('/Users/waverider/Desktop/Programming/Advent of Code/Day 3/input') as i:
    lines = i.readlines()
    lines = [line.rstrip() for line in lines]
    

def powerconsump(lines):
    gamma = ['0'] * 12
    epsilon = ['0'] * 12
    bitcountergamma = 0
    zerocountergamma = 0
    
    for bitpos in range(12):
        bitcountergamma = 0
        zerocountergamma = 0
        
        for x in range(len(lines)):
            if int(lines[x][bitpos]) > 0:
                bitcountergamma += 1
            else:
                zerocountergamma += 1
                
        if zerocountergamma > bitcountergamma:
            gamma[bitpos] = '0'
            epsilon[bitpos] = '1'
        else:
            gamma[bitpos] = '1' 
            epsilon[bitpos] = '0'
            
            
    print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))      
    
def airscrub(lines):
    oxset = lines
    co2set = lines
    for bitpos in range(12):
        oxset = countbits(bitpos, oxset, True)
            
    for bitpos2 in range(12):
        co2set = countbits(bitpos2, co2set, False)
            
    #return int(oxset[0], 2) * int(co2set[0], 2)
    return (int(oxset[0], 2) * int(co2set[0], 2))
            

def countbits(pos, input, greater):
    oneset = []
    zeroset = []
    
    if len(input) >= 2:
        for x in input:
            if x[pos] == '0':
                zeroset.append(x)

            elif x[pos] == '1':
                oneset.append(x) 
        
        print ((len(oneset), len(zeroset)))
        if greater == True:
            if len(zeroset) > len(oneset):
                return zeroset
            else:
                return oneset
        elif greater == False:
            if len(zeroset) > len(oneset):
                return oneset
            else:
                return zeroset  
    else:
        return input
            
print(airscrub(lines))