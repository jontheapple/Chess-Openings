import os
import random
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
	# Use a breakpoint in the code line below to debug your script.
	print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	os.chdir("Openings\\Black")
	contents = os.listdir()
	while len(contents) > 0:
		for content in contents:
			if content.endswith(".txt"):
				myMove = input("Enter your move, Yugi boy: ")
				if myMove == "Give Up":
					print("Your move is " + content)
				while myMove + ".txt" != content:
					myMove = input("Try again, Yugi boy: ")
					if myMove == "Give Up":
						print("Your move is " + content)
				contents.remove(content)

		if len(contents) == 0:
			break
		nextMove = random.randint(0, len(contents)-1)
		print("I play " + contents[nextMove])
		os.chdir(contents[nextMove])
		contents = os.listdir()

	print("Reached end of opening")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
