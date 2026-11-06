word = "programing"
# outer loop select one character at a time
for character in word: 
    count = 0
    #inner loop checks every character in the text
    for letter in word:
        if character == letter:
            count = count + 1
    print(f"{character} appears {count} time.")
