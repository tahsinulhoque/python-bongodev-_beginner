def capitalize_words(text):
    words = text.split()
    capitalized = [word[0].upper() + word[1:] if word else "" for word in words]
    return ' '.join(capitalized)

# Test
input_text = "python for web developers"
output = capitalize_words(input_text)
print(output)  # Output: Python For Web Developers
