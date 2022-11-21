len=int(input("how many numbers you want to store?"))
input_value_list=[]
for num in range(0,len):
    input_value=int(input("enter a value"))
    if input_value>=100:
        input_value_list.append("over")
    else:
        input_value_list.append(input_value)
print(input_value_list)
    
