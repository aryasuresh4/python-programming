def createFactorslist(number):
    for i in range(1,number+1):
        if number%i==0:
            print("{} \t".format(i),end=" ")
num=int(input("Enter a number to print it's factors list:"))
createFactorslist(num)