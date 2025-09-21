for n in range(1,101):
    seen = set() 
    num=n
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    if num == 1:
        print(n,end=" ")
