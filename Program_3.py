# Qn 2: Odd number series , increment when value is odd

def OddseriesModify(n):
    if n%2==0:
        n-=1
    value=1
    for i in range(n):
        print(value,end=" ")
        value+=2

n=int(input("Enter the number of times to be printed "))
OddseriesModify(n)