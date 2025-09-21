num=int(input())
seen = set() 
while num != 1 and num not in seen:
   seen.add(num)
   num = sum(int(i) ** 2 for i in str(num))
print(num == 1)