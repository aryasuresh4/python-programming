def charFreq(str):
    wordCount=dict()
    for letter in set(str):
        wordCount[letter]=str.count(letter)
    return wordCount
word=input("Enter a string to check for charecter frequency:")
print(charFreq(word))

//output
Enter a string to check for charecter frequency:arya
{'a': 2, 'r': 1, 'y': 1}
