winning_number = 9
user_input = int(input("Guess a number b/w 1 to 10: "))
if user_input == winning_number:
	print("You Win!")
else:
	print("You Lose, Try Again!")
