#Welcome message of quadratic equation solver
print('Welcome to the Quadratic Equation Solver App')
import cmath

print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solution can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

equations=(int(input("How many equations would you like to solve today: ")))

#Get user input
for equation in range(equations):
    print("\nSolving equation #" +str(equation+1))
    print("-------------------------------------------------------------------")
    a=float(input("Please enter your value of a (coefficient of x^2): "))
    b=float(input("Please enter your value of b (coefficient of x): "))
    c=float(input("Please enter your value of c (coefficient): "))

    print("\nThe solutions to " +str(a) +" x^2 + " + str(b) + " x + " + str(c)+ "= 0 are: ")


    #Print solution
    x1=(-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2=(-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)

    print("\n\t x1= " + str(x1))
    print("\n\t x2= " +str(x2))

    print("\nThanks for using the Quadratic Equation Solver App.Goodbye!!!!")
