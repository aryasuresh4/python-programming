class bank:
	def __init__(self,a,n,t,b):
		self.ac=a
		self.name=n
		self.type=t
		self.bal=b
	def deposite(self,a1):
		self.bal +=a1
		print("Balance:",self.bal)
	def withdraw(self,a2):
			self.bal-=a2
			print("Balance:",self.bal)
	def disp(self):
		print("Account number:",self.ac)
		print("Account name:",self.name)
		print("Account type:",self.type)
		print("Account balance:",self.bal)

print("WELCOME TO MY BANK")
print("----------------------")
a=int(input("Enter account number:"))
n=input("Enter account name:")
t=input("Enter account type:")
b=int(input("Enter initial account balance:"))
obj1=bank(a,n,t,b)
obj1.disp()
a1=int(input("Enter the amount to  deposite:"))
obj1.deposite(a1)
a2=int(input("Enter the amount to be withdraw:"))
obj1.withdraw(a2)




