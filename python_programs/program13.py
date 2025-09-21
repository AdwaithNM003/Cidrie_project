def is_leap(y):
    return (y%4==0 and y%100!=0) or (y%400==0)
if __name__=="__main__":
    y=int(input("Year: "))
    print(is_leap(y))
