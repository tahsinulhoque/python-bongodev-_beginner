def reverse_string(input_str):
    reversed_str = ""
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str

# Test
input_text = "bongodev"
output = reverse_string(input_text)
print(output)  # Output: vedognob
