# Input: Get the number for which to calculate the factorial
num = int(input("Enter a number: "))

# Initialize a variable to store the factorial
factorial = 1

# Check if the input is negative, zero, or positive
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate the factorial using a for loop
    for i in range(1, num + 1):
        factorial *= i

    # Output the result
    print(f"The factorial of {num} is {factorial}")
