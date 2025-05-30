import string

def is_palindrome(text):
    # Normalize: lowercase, remove spaces & punctuation
    normalized = ''.join(
        char.lower() for char in text if char.isalnum()
    )
    return normalized == normalized[::-1]

# Test
input_text = "Madam"
output = is_palindrome(input_text)
print(output)  # Output: True
