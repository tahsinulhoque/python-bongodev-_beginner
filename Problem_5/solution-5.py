def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))  # Recursive call
        else:
            flat.append(item)
    return flat

# Test
input_list = [1, [2, 3], [4, [5]]]
output = flatten_list(input_list)
print(output)  # Output: [1, 2, 3, 4, 5]
