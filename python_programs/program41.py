s=input("String: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
ops=""
for ch in s:
    if ch not in punctuations:
        ops+=ch
print(ops)