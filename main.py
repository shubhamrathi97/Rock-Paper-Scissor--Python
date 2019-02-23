import random
import os

record = []

def game_logic():
	print("Please Choose")
	print("1.rock")
	print("2.paper")
	print("3.scissor")
	choice = int(input())

	if choice == 1:
		choice_name = 'rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'

	print("user choice is: " + choice_name)

	comp_choice = random.randint(1, 3)

	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	if comp_choice == 1:
		comp_choice_name = 'rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'

	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)

	# condition for winning
	if ((choice == 1 and comp_choice == 2) or
			(choice == 2 and comp_choice == 1)):
		print("paper wins => ", end="")
		result = "paper"

	elif ((choice == 1 and comp_choice == 3) or
			  (choice == 3 and comp_choice == 1)):
		print("Rock wins =>", end="")
		result = "Rock"
	else:
		print("scissor wins =>", end="")
		result = "scissor"

	# Printing either user or computer wins
	if result == choice_name:
		winner = "User"
		print(" User wins ")
	else:
		winner = "comp"
		print(" Computer wins ")
	game_record_dict = {"u_choice": choice_name, "c_choice": comp_choice_name, "winner": winner}
	record.append(game_record_dict)

def start_game():
	print("Press 1 to start game")
	print("Press 2 to view stats")
	user_input = int(input())
	if user_input == 2:
		show_stats()
		return
	elif user_input == 1:
		print("Winning Rules of the Rock paper scissor game as follows: \n"
				  + "Rock vs paper->paper wins \n"
				  + "Rock vs scissor->Rock wins \n"
				  + "paper vs scissor->scissor wins \n")
		game_logic()
	else:
		print("Wrong input!")
		start_game()

def show_stats():
	i=1
	for r in record:
		print("====================== Game "+ str(i)+ "=============================")
		print("User Choice = " + r["u_choice"] )
		print("Computer Choice = " + r["c_choice"])
		print("User Choice = " + r["winner"])
		print("===================================")
		i+=1

def main():
	while True:
		start_game()
		print("Do you want to play again? (Y/N)")
		ans = input()
		# if user input n or N then condition is True
		if ans.lower() == 'n':
			print("Do you want to see result stats? (Y/N)")
			ans = input()
			# if user input n or N then condition is True
			if ans.lower() == 'y':
				show_stats()
			break

		os.system('cls')

if __name__ == "__main__":
	main()