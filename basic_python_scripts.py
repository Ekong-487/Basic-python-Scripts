print("Hello, World!")


# Function to calculate the sum of two numbers
def sum_numbers(a, b):
    return a + b

# Test the function
num1 = 10
num2 = 20
result = sum_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)



# Function to find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# Test the function
num1 = 10
num2 = 20
num3 = 15
maximum = max_of_three(num1, num2, num3)
print("The maximum of", num1, ",", num2, ", and", num3, "is:", maximum)



def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Test the function
number = 25
result = check_even_odd(number)
print("The number", number, "is", result)

# Function to calculate the factorial of a number
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Test the function
number = 5
result = factorial(number)
print("The factorial of", number, "is:", result)

