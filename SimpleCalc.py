# Simple Calculator

# A simple calculator that performs basic arithmetic operations based on user input
def simple_calc(var1, var2, sign):
    if(sign == '+'): 
        print(f"The sum of {var1} and {var2} is: {float(var1) + float(var2)}")
    elif(sign == '-'):
        print(f"The difference of {var1} and {var2} is: {float(var1) - float(var2)}")
    elif(sign == '*'):
        print(f"The product of {var1} and {var2} is: {float(var1) * float(var2)}")
    elif(sign == '/'):
        print(f"The quotient of {var1} and {var2} is: {float(var1) / float(var2)}")
    elif(sign == '%'):
        print(f"The remainder of {var1} and {var2} is: {float(var1) % float(var2)}")

# Function to check if the user wants to continue using the calculator
def check_continue():
    response = input("Do you want to perform another calculation? (yes/no):").lower().strip()
    if(response != "yes"): 
        print("Thank you for using the calculator. Goodbye!")
        return False
    return True 

ok = True 
while ok:
    # The variables to store the user's inputs to perform the calculation
    var1 = input("Enter First Number: ")
    var2 = input("Enter Second Number: ")

    # The variable to store the operation to be performed and the list of valid operations
    sign = input("Enter the operation (+, -, *, /, %): ")
    signs = ['+', '-', '*', '/', '%']

    # Check if the entered operation is valid and perform the calculation if it is
    if sign in signs: 
        simple_calc(var1, var2, sign)

        # Ask the user if they want to perform another calculation
        ok = check_continue()
    else: 
        print("Invalid operation. Please try again.")