import random
from time import sleep

snakes = {32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78}
ladders = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}

def roll_dice():
	return random.randint(1,6)

win = 100
player = 0
counter = 0

while True:
	steps = roll_dice()
	print("You Got:", steps)
	if player + steps == 100:
		break

	if (player + steps) > 100:
		player = player

	elif (player+steps) in ladders:
		print(f"LADDER ^ {player+steps} To {ladders[(player+steps)]}")
		player = ladders[(player+steps)]
	elif (player+steps) in snakes:
		print(f"SNAKE ~~ {player+steps} To {snakes[(player+steps)]}")
		player = snakes[(player+steps)]
	else:
		player += steps

	counter += 1
	print("Current Position:", player)
	print("***************\n")

print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"~~~~~~~ Congratulations !!! You won in {counter} steps ~~~~~~~".rjust(58))
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

