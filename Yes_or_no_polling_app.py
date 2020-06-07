#Welcome to the Yes or No Polling App
print("Welcome to the Yes or No Issue Polling App")

#Gather user input
issue=input("What is the yes or no issue you will be voting on today: ")
vote_numbers=int(input("What is the number of voters you will allow on the issue: "))
password =input("Enter a password for the polling result: ")

#initialize variable
yes =0
no = 0
results = {}

#Simulating voting
for i in range(vote_numbers):
    name=input("\nEnter your full name: ").title().strip()
    if name in results.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print("Here is our issue: " + issue)
        choice=input('What do you think .... yes or no: ').lower().strip()
        if choice == 'yes' or choice == 'y':
            choice='yes'
            yes +=1
        elif choice == 'no' or choice == 'n':
            choice='no'
            no+=1
        else:
            print("That is not a yes or no answer , but okay....")
        #Add vote to the dictionary results
        results[name]=choice
        print("Thank you " + name + "! Your vote of " + results[name] + " has been recorded.")

#Show who actually voted
total_votes=len(results.keys())
print("\nThe following " +str(total_votes) + " people voted.")
for keys in results.keys():
    print(keys)
#Summerize the voting results
print("\nOn the following issue: " + issue)
if yes>no:
    print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no>yes:
    print("No wins! " +str(no) + " votes to " + str(yes) + ".")
else:
    print("It was a tie! "+ str(no) + " votes to " + str(yes) + ".")

#Allow the issue creator to see the actual votes  
guess = input("\nTo see the voting results enter the admin password: ")
if guess == password:
    for key,value in results.items():
        print("Voters: " + key + "\t\t\tVote: " + value)
else:
    print("Sorry, that is not the correct password. GoodBye....")
print("\nThank you for using the Yes or No Issue Polling App.")