def find_duplicates(tag_list):
    seen = set()
    duplicates = set()
    
    for tag in tag_list:
        if tag in seen:
            duplicates.add(tag)
        else:
            seen.add(tag)
    
    return list(duplicates)

# Test
input_tags = ["ai", "ml", "python", "ml", "dl", "ai"]
output = find_duplicates(input_tags)
print(output)  

# Output: ['ml', 'ai']