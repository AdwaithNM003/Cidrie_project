s=input("Sentence: ")
ws=s.split(); ws.sort(key=str.lower)
for w in ws: 
    print(w)
