word=input("Enter a word:")
vowels=["a","e","i","o","u"]
list1=[]
for i in word:
	if(i in word and i not in vowels):
		list1.append(i)
print("The consonents in list are:",list1)
