arr=input("Array: ").split()
d=int(input("d: "))
print(arr[d%len(arr):]+arr[:d%len(arr)])
