s=input("String: ")
i=int(input("Index to remove (0-based): "))
print(s[:i]+s[i+1:] if 0<=i<len(s) else s)
