 #Rock,Paper , Scissors Program

import random

print("Welcome to the game of Rock,Paper , Scissors")

#Get user input
rounds = int (input("\nHow many rounds would you like to play: "))

#Variables Initialize
moves=['rock','paper','scissors']
p_scores=0
c_scores=0

#The main part of the game
for game_round in range(rounds):
    #Print the main game screen and get user input
    print("\nRound " + str(game_round+1))
    print("\nPlayer: " + str(p_scores) + "\tComputer: " + str(c_scores))

    #Get computer move
    c_index=random.randint(0,2)
    c_choice=moves[c_index]

    #Get the player move
    p_choice=input("Time to pick.... rock,paper,scissors: ").lower()

    #If the player makes a valid move
    if p_choice in moves:
        print("\tComputer: " + c_choice)
        print("\tPlayer: " +p_choice)

        #Computer choose rock
        if p_choice =='rock' and c_choice=='rock':
            winner='tie'
            phrase='It is a tie, how boring'
        elif p_choice=='paper' and c_choice=='rock':
            winner='player'
            phrase="Paper covers rock!"
        elif p_choice=='scissors' and c_choice=='rock':
            winner='computer'
            phrase='Rock smashes scissors!'
        
        #Computer choose paper
        elif p_choice=='rock' and c_choice=='paper':
            winner='computer'
            phrase='Paper covers rock'
        elif p_choice=='paper' and c_choice=='paper':
            winner='tie'
            phrase='It is a tie,How boring'
        elif p_choice=='scissors' and c_choice=='paper':
            winner='player'
            phrase="Scissors cut Paper"
        
        #Computer choose scissor
        elif p_choice=='rock' and c_choice=='scissors':
            winner='player'
            phrase='Rock smashes scissors!'
        elif p_choice=='paper' and c_choice=='scissors':
            winner='scissors'
            phrase="scissors cut paper"
        elif p_choice=='scissors' and c_choice=='scissors':
            winner='tie'
            phrase="It is a tie,how boring"
        else:
            print("Round winner not calculated.")
            winner='tie'
            phrase='It is a tie,how boring.'

#Display round result
        print("\t" +phrase)
        if winner=='player':
            print("\tYou win round " + str(game_round+1)+ ".")
            p_scores+=1
        elif winner=='computer':
            print("\tComputer wins round " +str(game_round+1) + ".")
            c_scores+=1
        else:
            print("\tThis round was a tie.")
    else:
        print("That is not a valid game option!")
        print("Computer gets the point!")
        c_scores +=1
#Game has ended , print results
print("\nFinal Game Results")
print("\tRounds Played: " + str(rounds))
print("\tPlayer Score: " + str(p_scores))
print("\tComputer Score: " + str(c_scores))
if p_scores>c_scores:
    print("\tWinner: Player!!")
elif c_scores>p_scores:
    print("\tWinner: Computer :-)")
else:
    print("\tThe game was a tie.")