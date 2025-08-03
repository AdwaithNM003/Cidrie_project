num1=set()
million_list=[]
for i in range(1,1000001):
    million_list.append(i)
tar=int(input("enter target num: "))
print(million_list)
for i in million_list:
    num2=tar-i
    if num2 in num1:
       print("has a pair")
    else:
        num1.add(i)
