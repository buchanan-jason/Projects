def calculate():
    # Perform calculation
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Collect input of two integers
num1 = input("Enter 1st number\n:")
num2 = input("Enter 2nd number\n:")

# Convert strings to integers
num1 = int(num1)
num2 = int(num2)

result = calculate()
print(result)








