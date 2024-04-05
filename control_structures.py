#odd or even using if-else
print ("Check if a number is odd or even")
number = int(input("Enter a number:"))
if (number % 2 == 0):
    print ( f"{number} is even")
else :
    print ( f"{number} is odd")


#Largest among three numbers using if-else statements
print("\n Largest of three numbers")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if (num1>=num2 and num1>=num3):
    print(f"{num1}is the largest number")
elif (num2>=num1 and num2>=num3):
    print(f"{num2}is the largest number")
else:
    print(f"{num3}is the largest number")
