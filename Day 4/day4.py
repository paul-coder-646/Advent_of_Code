import sys

# This Day I needed some inspiration from Roman, a friend of mine, 
# who is also doing AoC this year (Github: @romern), so this code is NOT really mine :D

def parse_input(input_string):
    
    # rstrip prevents empty lines at the end of the input from being mixed up with the input
    input_string = input_string.rstrip("\n").split("\n")
    number_order = [int(i) for i in input_string[0].split(",")]
    bingo_length = len(input_string[2].split())
    # bingo_field_amount determines how many bingo boards there are        
    bingo_field_amount = int((len(input_string)-1)/(bingo_length+1))
    
    #group all bingo boards together 
    bingo_fields = []
    for i in range(bingo_field_amount):
    	cur_field = []
    	for j in range(bingo_length):
            # go through all bingo rows and add them to the list
    		row_index = 2 + i*(bingo_length+1) + j
    		cur_field.append([int(k) for k in input_string[row_index].split()])
    	bingo_fields.append(cur_field)
    print(bingo_fields)
    return number_order,bingo_fields


def sum_all_unmarked(bingo_field, drawn_numbers):
	return sum(n for l in bingo_field for n in l if n not in drawn_numbers)


# Checks if a bingo field is winning, and returns its score
def check_bingo_field(bingo_field, drawn_numbers):
	for i in range(len(bingo_field)):
		row = bingo_field[i]
		col = [b[i] for b in bingo_field]
		winner_row = True
		winner_col = True
  
		for j in range(len(bingo_field)):
			if row[j] not in drawn_numbers:
				winner_row = False
			if col[j] not in drawn_numbers:
				winner_col = False
		if winner_row or winner_col:
			return True, sum_all_unmarked(bingo_field, drawn_numbers)*drawn_numbers[-1]
	return False, 0


def part1(number_order, bingo_fields):
	round = 1
	while True:
		for i,b in enumerate(bingo_fields):
			win, score = check_bingo_field(b, number_order[:round])
			if win:
				return f"Board {i} won with {score} points in round {round}!"
		round += 1

def part2(number_order, bingo_fields):
	round = 0
	bingo_fields = {i:b for i,b in enumerate(bingo_fields)}
	while len(bingo_fields)>0:
		round += 1
		remove_fields = []
		for i in bingo_fields:
			b = bingo_fields[i]
			win, score = check_bingo_field(b, number_order[:round])
			if win:
				remove_fields.append(i)
		for i in remove_fields:
			if len(bingo_fields)==1:
				return f"The last board to win is Board {list(bingo_fields.keys())} with {score} points in round {round}"
			del bingo_fields[i]
	return "mhmm, undefined behaviour"


if __name__ == "__main__":
    number_order, bingo_fields = parse_input(open('/Users/waverider/Desktop/Programming/Advent of Code/Day 4/input').read()) 
    print(part1(number_order,bingo_fields))
    print(part2(number_order,bingo_fields))
    