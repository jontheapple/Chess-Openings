import os
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
	# Use a breakpoint in the code line below to debug your script.
	print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	with open('add.txt') as f:
		# Determine what color I am playing as
		os.chdir("Openings")
		myColor = ""
		line = f.readline()
		if line[0] == "W":
			os.chdir("White")
			myColor = "W"
		elif line[0] == "B":
			os.chdir("Black")
			myColor = "B"
		else:
			print("wtf did u do?")
			exit()

		# Start reading chess moves
		line = f.readline()
		moveNum = 1
		while bool(line):
			if line == "\n":
				break
			moves = line.split()
			if myColor == "W":
				currentLines = os.listdir()
				myMove = ""
				for content in currentLines:
					if content.endswith(".txt"):
						myMove = content
				if bool(myMove) and myMove != moves[1] + ".txt":
					print("You're trying to add a different move than what you already play, at move " + str(moveNum))
					print("The move you already play is " + myMove)
					print("The move you are trying to add is " + moves[1])
					exit()
				move = open(moves[1] + ".txt", "w+")
				if len(moves) > 2:
					if os.path.exists(moves[2]):
						pass
					else:
						os.makedirs(moves[2])
					os.chdir(moves[2])
			else:
				if os.path.exists(moves[1]):
					pass
				else:
					os.makedirs(moves[1])
				os.chdir(moves[1])
				currentLines = os.listdir()
				myMove = ""
				for content in currentLines:
					if content.endswith(".txt"):
						myMove = content
				if bool(myMove) and myMove != moves[2] + ".txt":
					print("You're trying to add a different move than what you already play, at move " + str(moveNum))
					print("The move you already play is " + myMove)
					print("The move you are trying to add is " + moves[2])
					exit()
				move = open(moves[2] + ".txt", "w+")

			moveNum += 1
			line = f.readline()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
