#Challenge 17:Coin Toss app
import random
#Welcome Message
print("Welcome to the Coin Toss App")

#Gather user input
print("\nI will flip  a coin a set number of times.")
flip_number=int(input("\nHow many times would you like me to flip the coin: "))
choice=input("\nWould you like to see the result of each flip(y/n): ").lower()

print("\nFlipping....")
heads=0
tails=0
for flip in range(flip_number):
   
    coin = random.randint(0,1)
    if coin == 1:
        heads +=1
        if choice.startswith('y'):
            print("Head")
    else:
        tails +=1
        if choice.startswith('y'):
            print("Tails")
    if heads==tails:
        print("At " +str(flip+1)+ " flips,the number of heads and tails were equal at " + str(heads) + " each.")

#Calculation
heads_percentage=round(100*heads/flip_number,2)
tails_percentage=round(100*tails/flip_number,2)

#Display on screen

print("\nResults of Flipping A Coin " + str(flip_number) + " Times.")

print("\nSide\t\tCount\t\tPercentage")
print("\nHeads\t\t" +str(heads)+"/"+str(flip_number) +"\t\t"+ str(heads_percentage) + "%")
print("\nTails\t\t" +str(heads)+"/" +str(flip_number)+"\t\t"+ str(heads_percentage) + "%")