def addingOrly(str):
    if(str[-3:]=="ing"):
        str=str+"ly"
    else:
        str=str+"ing"
    return str
word=input("Enter a word to modify:")
modifiedString=addingOrly(word)
print("Modified string=",modifiedString)

//output
Enter a word to modify:going
Modified string= goingly
