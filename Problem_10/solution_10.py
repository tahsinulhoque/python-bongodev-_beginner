import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test
input_number = 29
output = is_prime(input_number)
print(output)  # Output: True
