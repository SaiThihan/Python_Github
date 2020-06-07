#Welcome to the Word counter program
from collections import Counter
print("Welcome to the word counter program")

#List of elements to remove from all text for analysis
non_letters=['1','2','3','4','5','6','7','8','9','0',' ',
'.','?','!',',','"',':',"'",'(',')','%','$','&','#','\n','\t']

#Info for all non letters form key_phrase_1
key_phrase_1=input("Enter a word or phrase to count the occurrence of each letter: ").lower().strip()

#Removing all non letters form key_phrase_1
for non_letter in non_letters:
    key_phrase_1=key_phrase_1.replace(non_letter, '')
total_occurences=len(key_phrase_1)

#Create a counter object totally the number of each letter
letter_count=Counter(key_phrase_1)

#Determine the word_counter for the message
print("\nHere is the Word counter from key_phrase_1: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key,value in sorted(letter_count.items()):
    percentage=100*value/total_occurences
    percentage=round(percentage,2)
    print("\t"+ key + "\t\t" + str(value) + "\t\t" + str(percentage) + "%")

#Make a list of letters from highest occurence to lowest
ordered_letter_count=letter_count.most_common()
key_phrase_2_ordered_letters=[]
for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])

#Print the list
print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_2_ordered_letters:
    print(letter,end=' ')