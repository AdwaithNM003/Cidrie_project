arr=input("Array: ").split()
k=int(input("k: "))
print(arr[k%len(arr):]+arr[:k%len(arr)])
