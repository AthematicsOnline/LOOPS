# Define a range of numbers to check for prime numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime Numbers in the Range:")
# Iterate through the range using a for loop
for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)
