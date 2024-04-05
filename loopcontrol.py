#usage of continue statement
print ("usage of continue statement")
# Iterate over the numbers from 1 to 10
for num in range(1, 11):
    # Check if the number is 5
    if num == 5:
        # Skip the number 5 and continue to the next iteration
        continue
    # Print the number if it's not 5
    print(num)

#usage of break statement
print("Usage of break statement")
# Initialize variables
total = 0
num = 1

# Iterate over the numbers from 1 to 100
while num <= 100:
    # Add the current number to the total
    total += num
    # Check if the sum exceeds 1000
    if total > 1000:
        # If the sum exceeds 1000, break out of the loop
        break
    # Increment the number
    num += 1

# Print the sum
print("Sum of numbers from 1 to 100:", total)

