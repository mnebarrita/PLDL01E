from file1 import ArithmeticOperations # to access the codes written within file1.py

# instantiate the class inside the file1.py
obj = ArithmeticOperations()

# getting inputs from the user
num1 = int(input("Enter the value of number 1: "))
num2 = int(input("Enter the value of number 2: "))

# formulating formula and access the attributes under the class ArithmeticOperations
# the input data for num1 and num2 variables will be the value of the parameter variables
# under the attributes of the class ArithmeticOperations
sum = obj.get_sum(num1, num2)
difference = obj.get_difference(num1, num2)
product = obj.get_product(num1, num2)
quotient = obj.get_quotient(num1, num2)

# display the computed value for sum, difference, product, and quotient
print("Sum of two input numbers is: ", sum)
print("The difference of the two inputted numbers is: ", difference)
print("The product of two inputted numbers is: ", product)
print("The quotient of two inputted numbers is: {:.2f}".format(quotient))