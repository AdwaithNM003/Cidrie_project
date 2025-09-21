a=input("A: ")
b=input("B: ")
print(list(set(a.split())^set(b.split())))
