num1=int(input("Enter a integer"))
num2=int(input("Enter a integer"))
num3=int(input("Enter a integer"))
if(num1>=num2)and(num1>=num3):
    largest=num1
elif(num2>=num1)and(num2>=num3):
    largest=num2
else:
    largest=num3
print("the biggest number is:",largest)
         
