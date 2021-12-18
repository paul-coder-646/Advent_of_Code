def mvessel():
    depth = 0
    horizontal = 0
    aim = 0
    with open('/Users/waverider/Desktop/Programming/Advent of Code/Day 2/input') as i:
        lines = i.readlines()
        
    lines = [line.rstrip() for line in lines]
    lines = [x.split() for x in lines]
    
    for op in lines:
        if op[0] == "forward":
            horizontal += int(op[1])
            depth += (aim * int(op[1]))
        elif op[0] == "down":
            aim += int(op[1])
        elif op[0] == "up":
            aim -= int(op[1])
   
    print(f'the result is ' + str((horizontal * depth)))

mvessel()