from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)
    return list(anagram_dict.values())

# Test
input_words = ["bat", "tab", "cat", "act"]
output = group_anagrams(input_words)
print(output)  # Output: [['bat', 'tab'], ['cat', 'act']]
