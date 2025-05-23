def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count

# Test
input_text = "Data Science is awesome"
output = count_vowels(input_text)
print(output)  # Output: 9
