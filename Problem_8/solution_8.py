def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

# Test
input_number = 5
output = factorial(input_number)
print(output)  # Output: 120
