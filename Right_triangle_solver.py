#Welcome Message
import math
print("Welcome to the Right Triangle Solver App")

#get user input
first_leg=float(input("What is the first leg of the triangle: " ))
second_leg=float(input("What is the second leg of the triangle: "))

#Calculation
hypo_side=math.sqrt(first_leg**2 + second_leg **2 )
hypo_side=round(hypo_side,3)

area_side=(1/2)*first_leg*second_leg
area_side=round(area_side,3)

#answer
print("\nFor a triangle with legs of " + str(first_leg) + " and" + str(second_leg) + "the hypotenuse is " + str(hypo_side))
print("\nFor a triangle with legs of " + str(first_leg) + " and" + str(second_leg) + "the area is " + str(area_side))