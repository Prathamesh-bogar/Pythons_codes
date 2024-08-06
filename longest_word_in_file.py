def longest_word_with_no_repeat_char(filepath):
    with open(filepath, 'r') as file:
        f = file.read()
    words = f.split("\n")

    longest_word = ""
    max_length = 0

    for word in words:
        if len(set(word)) == len(word):
            if len(word) > max_length:
                longest_word = word
                max_length = len(word)
                
    return longest_word


file_path = 'C:/Users/hp/Desktop/Sayali/demo.txt'
result = longest_word_with_no_repeat_char(file_path)
print(f"The longest word with uniqu characters is {result}")