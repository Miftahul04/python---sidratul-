import keyword
#Printing the list of keywords
print(keyword.kwlist)
#checking whether its a keyword or not
word = input ("Enter a keyword ")
print(keyword.iskeyword(word))