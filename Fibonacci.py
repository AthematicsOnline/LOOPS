# Define the number of terms in the Fibonacci sequence
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Initialize variables for the first two terms
first_term, second_term = 0, 1

# Print the first two terms
print("Fibonacci Sequence:")
print(first_term)
print(second_term)

# Generate the remaining terms using a for loop
for _ in range(2, num_terms):
    next_term = first_term + second_term
    print(next_term)
    first_term, second_term = second_term, next_term
