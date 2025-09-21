def armstrongs(l,h):
    return [n for n in range(l,h+1) if sum(int(d)**len(str(n)) for d in str(n))==n]
if __name__=="__main__":
    print(armstrongs(int(input("Low: ")), int(input("High: "))))
