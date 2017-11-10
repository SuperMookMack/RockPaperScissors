import random
def playgame():
	while True:
		player_move = input("R for Rock, P for Paper, S for Scissors, Q to quit\n")
		computer_choices = ['R','P','S']
		computer_move= random.choice(computer_choices)
		
		if not validMove(player_move):
			continue
		if player_move == computer_move:
			print("It's a tie!")
		elif player_move == 'R' and computer_move == 'P':
			print("You lose!")
		elif player_move == 'P' and computer_move == 'S':
			print("You lose!")
		elif player_move == 'S' and computer_move == 'R':
			print("You lose!")
		elif player_move == 'Q':
			break
		
		else:
			print("You win!")
	
	
def validMove(player_move):
	if player_move in ['P', 'R', 'Q', 'S']:
		return True
	return False
def Main():
	print("Rock, Paper, Scissors Game!")
	while True:
		choice = int(input("Type 1 to Play or 2 to quit\n"))
		
		if choice==2:
			print("Thanks for playing!")
			break
		if choice==1:
			playgame()
		else:
			print("Invalid Choice")
			print (choice)
	
	

Main()