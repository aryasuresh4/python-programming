def findLongestWord(wordList):
    highestLength=0
    for word in wordList:
        if(len(word)>highestLength):
            highestLength=len(word)
    return highestLength
words=input("Enter a series of words seperated by spaces:").split(" ")
print(findLongestWord(words))

//output
Enter a series of words seperated by spaces:arya anandalakshmi megha anju
13
