arr=list(map(int,input("Array: ").split()))
print(all(arr[i]<=arr[i+1] for i in range(len(arr)-1)) or all(arr[i]>=arr[i+1] for i in range(len(arr)-1)))
