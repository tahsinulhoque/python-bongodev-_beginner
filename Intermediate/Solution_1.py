def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Test
input_sentence = "Machine learning is fascinating"
output = longest_word(input_sentence)
print(output)  # Output: fascinating
