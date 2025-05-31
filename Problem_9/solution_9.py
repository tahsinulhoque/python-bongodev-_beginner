def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Test
input_number = 9875
output = sum_of_digits(input_number)
print(output)  
# Output: 29


def sum_of_digits_math(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Test
print(sum_of_digits_math(9875))  # Output: 29
