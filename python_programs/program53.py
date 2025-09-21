nums=list(map(int,input("Numbers: ").split()))
uniq=sorted(set(nums), reverse=True)
print(uniq[1] if len(uniq)>1 else None)
