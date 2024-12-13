"hello".upper()
"Hello".lower()
"hello world".split()
# String Reverse
main_string = "Hello, World!"
reversed_string = main_string[::-1]
print(reversed_string)


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


# Input string
main_string = "Hello, World!"
vowel_count = count_vowels(main_string)
print(f"Vowel count: {vowel_count}")  # Output: Vowel count: 3
#Multiplication, division and %
x = 10
y = 3.5
print(x + y)
print(x // 2)
print(x % 3)


#How to check odd even
# Odd or Even Checker
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Input Number
num = int(input("Enter a number: "))
result = check_odd_even(num)
print(f"The number {num} is {result}.")
#FOR loop practice
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    #using else with for
for i in range(5):
    print(i)
else:
    print("Loop completed")
#while loop
count = 1

while count <= 5:
    print(count)
    count += 1  # Increment the counter
 #Python program that uses a for loop to calculate the sum of the first 10 natural numbers
    # Initialize sum
    total_sum = 0

    # Loop through the first 10 natural numbers
    for number in range(1, 11):  # range(1, 11) generates numbers from 1 to 10
        total_sum += number

   
    print("The sum of the first 10 natural numbers is:", total_sum)
 #uses a while loop to print numbers from 1 to 100, breaking the loop if the number is divisible by 7
    # Initialize the starting number
    number = 1

  
    while number <= 100:
        
        print(number)

        
        if number % 7 == 0:
            print("Breaking the loop as the number is divisible by 7.")
            break

        
        number += 1
 #Python program that uses a for loop to print the multiplication table of a given number
    # Input: Get the number from the user
    number = int(input("Enter a number to display its multiplication table: "))

    
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):  
        result = number * i
        print(f"{number} x {i} = {result}")

#practice on function 
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example usage
num = int(input("Enter a number: "))
result = factorial_iterative(num)
print(f"The factorial of {num} is {result}.")

#reverse string 
def reverse_string(s):
    return s[::-1]


input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")

