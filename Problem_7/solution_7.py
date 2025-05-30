def find_missing_number(logs):
    n = len(logs) + 1  # Total numbers including the missing one
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(logs)
    return expected_sum - actual_sum

# Test
input_logs = [1, 2, 4, 5]
output = find_missing_number(input_logs)
print(output)  # Output: 3
