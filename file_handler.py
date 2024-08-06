def longest_word_with_no_repeat(file_path):   
    def has_unique_chars(word):
        if len(set(word)) == len(word):
            return True
        else:
            return False
        
 
    longest_word = ""
    max_length = 0

    with open(file_path, "r") as file:
        f = file.read()
        words = f.split()
        for word in words:
            if has_unique_chars(word):
                if len(word) > max_length:
                    longest_word = word
                    max_length = len(word)
                    
    return longest_word


file_path = 'C:/Users/hp/Desktop/Sayali/demo.txt'
result = longest_word_with_no_repeat(file_path)
print(f"The longest word with no repeating chars is {result}")

