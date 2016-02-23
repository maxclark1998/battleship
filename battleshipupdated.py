from random import choice

"""Initiates game"""
print "Welcome to battleship!"
print "Menu:"
print "1. Single-player \n 2. Multi-player \n 3. Help \n 4. Credits \n"
game_choice = raw_input()

if game_choice == "1":

	"""makes a board"""
	rows = []
	for a in [0]:
		for b in [0]:
			for c in [0]:
				for d in [0]:
					for e in [0]:
						count = 0
						while(count <= 4):
							rows.append([a,b,c,d,e])
							count += 1
	
	for i in rows:
		for space in i:
			print space,
		print

	"""ship definition"""
	class ship(object):
		def __init__(self, x_pos, y_pos):
			self.x_pos = x_pos
			self.y_pos = y_pos

	"""sequence for ship placement choices"""
	possible_combos = []
	for x in range(0, len(rows[0])):
		for y in range(0, len(rows[0])):
			possible_combos.append([x, y])

	"""make and place ships"""
	first_choice = choice(possible_combos)

	first_ship = ship(first_choice[0], first_choice[1])

	if first_choice in possible_combos:
		possible_combos.remove(first_choice)
	
	second_choice = choice(possible_combos)

	second_ship = ship(second_choice[0], second_choice[1])

	if second_choice in possible_combos:
		possible_combos.remove(second_choice)

	third_choice = choice(possible_combos)

	third_ship = ship(third_choice[0], third_choice[1])

	if third_choice in possible_combos:
		possible_combos.remove(third_choice)
	
	fourth_choice = choice(possible_combos)

	fourth_ship = ship(fourth_choice[0], fourth_choice[1])

	if fourth_choice in possible_combos:
		possible_combos.remove(fourth_choice)
		
	"""list of ship positions"""
	places_of_ships = [first_choice[0], first_choice[1]], [second_choice[0], second_choice[1]], [third_choice[0], third_choice[1]], [fourth_choice[0], fourth_choice[1]]
	
	"""Let's play"""
	turn_count = 1
	win_count = 0
	while(turn_count <= 4):
		print "Turn " + str(turn_count)
		
		"""stores guesses"""
		print "Guess the ship's place."
		guess_x = int(raw_input("Guess an x coordinate between 1 and 5 \n"))
		guess_x -= 1
	
		guess_y = int(raw_input("Guess a y coordinate between 1 and 5 \n"))
		guess_y -= 1
	
		total_guess = [guess_x, guess_y]
		
		"""Checks to see where guess lands. Replaces correct spots with X and others remain same."""
		if total_guess in places_of_ships:
			rows[guess_y][guess_x] = 'X'
			for i in rows:
				for slot in i:
					print slot,
				print
			win_count += 1
	
		else:
			for i in rows:
				for slot in i:
					print slot,
				print
			print "Sorry! Try again"
			
		turn_count += 1

	"""Game over messages"""
	
	if win_count == 4:
		print "You win!"
	
	elif win_count >= 2:
		print "Good try!"
		
	else:
		print "Keep trying!"
		
elif game_choice == "2":
	"""multi-player game"""
	print "Welcome to battleship: 2 player!"

	"""Screen wiper for player privacy"""
	class Wipe(object):
    		def __repr__(self):
        		return '\n' * 1000

	wipe = Wipe()
	
	"""makes a board"""
	board_sizes = []
	for x in range(5, 10):
		for y in range(5,10):
		    if x == y:
			    board_sizes.append([x, y])
	
	print board_sizes

	print "Board sizes"
	print "1. 5 x 5 \n 2. 6 x 6 \n 3. 7 x 7 \n 4. 8 x 8 \n 5. 9 x 9 \n 6. 10 x 10"

	board_size = int(raw_input("Select a size \n"))
	
	board = []
	for i in range(board_size + 4):
		board.append([])
	
	for i in range(board_size + 4):
		for j in range(board_size + 4):
			board[j].append(0)	

	"""prints board"""
	for i in board:
		for slot in i:
			print slot,
		print

	"""possible places for ships"""
	possible_combos = []
	for x in range(0, board_size + 4):
		for y in range(0, board_size + 4):
			possible_combos.append([x,y])

	"""Ship definition"""

	class ship(object):
		def __init__(self, x_pos, y_pos, length):
			self.x_pos = x_pos
			self.y_pos = y_pos
			self.length = length

	"""player 1 ship selection"""
	print "Turn the computer to player 1"
	print "Time to select your ship positions!"
	
	"""Destroyer"""
	print "Destroyer: 2 space ship"
	p1_destroyer_x = int(raw_input("Choose starting point for destroyer. \n"))
	p1_destroyer_y = raw_input(("Choose starting point for destroyer. \n"))
	p1_destroyer_pos = [p1_destroyer_x, p1_destroyer_1]
	
	print "Choose a direction."
	p1_destroyer_dir = int(raw_input("1. Up \n 2. Down \n 3. Left \n 4. Right \n"))
	
	p1_destroyer = ship(p1_destroyer_x, p1_destroyer_y, 2)
	
	if p1_destroyer_pos in possible_combos:
		possible_combos.remove(p1_destroyer_pos)

	"""Cruiser"""
	print "Cruiser: 3 space ship"
	p1_cruiser_x = int(raw_input("Choose starting point for cruiser. \n"))
	p1_cruiser_y = int(raw_input("Choose starting point for cruiser. \n"))
	p1_cruiser_pos = [p1_cruiser_x, p1_cruiser_y]
	
	print "Choose a direction."
	p1_cruiser_dir = int(raw_input("1. Up \n 2. Down \n 3. Left \n 4. Right \n 5. Middle \n"))
	
	p1_cruiser = ship(p1_cruiser_x, p1_cruiser_y, 3)
	
	if p1_cruiser_pos in possible_combos:
		possible_combos.remove(p1_cruiser_pos)
		
	"""Submarine"""
	print "Submarine: 3 space ship"
	p1_submarine_x = int(raw_input("Choose starting point for submarine. \n"))
	p1_submarine_y = raw_input(("Choose starting point for submarine. \n"))
	p1_submarine_pos = [p1_submarine_x, p1_submarine_1]
	
	print "Choose a direction."
	p1_submarine_dir = int(raw_input("1. Up \n 2. Down \n 3. Left \n 4. Right \n 5. Middle \n"))
	
	p1_submarine = ship(p1_submarine_x, p1_submarine_y, 3)
	
	if p1_submarine_pos in possible_combos:
		possible_combos.remove(p1_submarine_pos)
		
	"""Battleship"""
	print "Battleship: 4 space ship"
	p1_battleship_x = int(raw_input("Choose starting point for battleship. \n"))
	p1_battleship_y = raw_input(("Choose starting point for battleship. \n"))
	p1_battleship_pos = [p1_battleship_x, p1_battleship_1]
	
	print "Choose a direction."
	p1_battleship_dir = int(raw_input("1. Up \n 2. Down \n 3. Left \n 4. Right \n 5. Middle \n"))
	
	p1_battleship = ship(p1_battleship_x, p1_battleship_y, 4)
	
	if p1_battleship_pos in possible_combos:
		possible_combos.remove(p1_battleship_pos)
		
	"""Aircraft carrier"""
	print "Aircraft carrier: 5 space ship"
	p1_carrier_x = int(raw_input("Choose starting point for carrier. \n"))
	p1_carrier_y = raw_input(("Choose starting point for carrier. \n"))
	p1_carrier_pos = [p1_carrier_x, p1_carrier_1]
	
	print "Choose a direction."
	p1_carrier_dir = int(raw_input("1. Up \n 2. Down \n 3. Left \n 4. Right \n 5. Middle \n"))
	
	p1_carrier = ship(p1_carrier_x, p1_carrier_y, 5)
	
	if p1_carrier_pos in possible_combos:
		possible_combos.remove(p1_carrier_pos)
		
	"""Builds player ones board"""
	p1_board = []
	for i in range(board_size + 4):
		p1_board.append([])
	
	for i in range(board_size + 4):
		for j in range(board_size + 4):
			p1_board[j].append(0)
			
	if p1_destroyer_dir == "1":
		p1_board[p1_destroyer_y][p1_destroyer_x] = "X"
		p1_board[p1_destroyer_y - 1][p1_destroyer_x] = "X"
	elif p1_destroyer_dir == "2":
		p1_board[p1_destroyer_y][p1_destroyer_x] = "X"
		p1_board[p1_destroyer_y + 1][p1_destroyer_x] = "X"
	elif p1_destroyer_dir == "3":
		p1_board[p1_destroyer_y][p1_destroyer_x] = "X"
		p1_board[p1_destroyer_y][p1_destroyer_x - 1] = "X"
	elif p1_destroyer_dir == "4":
		p1_board[p1_destroyer_y][p1_destroyer_x] = "X"
		p1_board[p1_destroyer_y][p1_destroyer_x + 1] = "X"
		
	
		
elif game_choice == "3":
	raise RuntimeError('Sorry, this option is not available yet.')
elif game_choice == "4":
	print "Battleship!"
	print "Programmed by Max Clark"
	print "Code help from /u/... to be continued when project is complete"