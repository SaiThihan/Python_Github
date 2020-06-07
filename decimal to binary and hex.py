#welcome message for Binary/Hexadecimal converter app
print("Welcome to the Binary/Hexadecimal Converter App")

#Gather user input
decimal_value=(int(input("Compute binary and hexadecimal values up to the following decimal number: ")))
binary=[]
hexadecimal=[]
decimal=list(range(1,decimal_value+1))

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating Lists.......Complete!")

#Using Slices portion

print("\nUsing slices, we will now show a portion of each list.")
low_range=(int(input("What decimal number would you like to start at: ")))
high_range=(int(input("What decimal number would you like to stop at: ")))


#Decimal Portion Slice
print("\nDecimal values from " + str(low_range) + " to " + str(high_range))
for num in decimal[low_range-1:high_range]:
    print(num)

#Binary portion slice
print("\nBinary values from " + str(low_range) + " to " + str(high_range))
for num in binary[low_range-1:high_range]:
    print(num)

#Hexadecimal Portion Slice
print("\nHexadecimal values from " + str(low_range) + " to " + str(high_range))
for num in hexadecimal[low_range-1:high_range]:
    print(num)

#Print Out the Whole List
input("Press Enter to see all values from 1 to " + str(decimal_value))
print("\nDecimal\t\t\tBinary\t\t\tHexadecimal")
print("---------------------------------------------------------------------------------")

for d,b,h in zip(decimal,binary,hexadecimal):
    print(str(d)+"\t\t\t" +str(b)+"\t\t\t" + str(h))