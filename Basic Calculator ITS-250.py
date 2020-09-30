#Math Calculator for basic functions and arithmetics
print("Select Arithmetic")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Putting the print and arithmetic options allows for a specifc function to be used
#These specific functions will add, subtract, multiply, and divide

while True:
    choice = input("Enter choice 1,2,3,4:")
    break
num1 = input("Enter a number: ")
num2 = input("Enter second number: ")

add = float(num1) + float(num2)
#code for setting "add" to the addition operation
subtract = float(num1) - float(num2)
#code for setting "Subtract" to the Subtraction operation
Multiply = float(num1) * float(num2)
#code for setting "Multiply" to the Multiplication operation
Divide = float(num1) / float(num2)
#code for setting "Divide" to the division operation

if choice == "1":
    print(add)
#setting "1" to addition allows this operation to execute the "add" function listed above
elif choice == "2":
    print(subtract)
#setting "2" to subtraction allows this operation to execute the "subtract" function listed above
elif choice == "3":
    print(Multiply)
#setting "3" to Multiplication allows this operation to execute the "multiply" function listed above
elif choice == "4":
    print(Divide)
#setting "4" to Division allows this operation to execute the "divide" function listed above
else:
    print("error")
#an error will occur if none of the listed function above are chosen

