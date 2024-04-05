print (" Factorial of a number")
# Get the number from the user
num = int(input("Enter a number: "))

# Initialize variables
factorial = 1
i = 1

# Calculate factorial using a while loop
while i <= num:
    factorial *= i
    i += 1

# Print the factorial
print("Factorial of", num, "is:", factorial)


print("Fibonacci series")
# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# Initialize variables for the first two terms
a, b = 0, 1

# Initialize a counter
count = 0

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to", n, "terms:")
    print(a)
else:
    print("Fibonacci series up to", n, "terms:")
    while count < n:
        print(a, end=" ")
        # Update variables to generate the next term
        fib_sum = a + b
        a = b
        b = fib_sum
        count += 1
