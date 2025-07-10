# Qn 2: Odd number series

def Oddseries(n):
    value=1
    for i in range(n):
        print(value,end=" ")
        value+=2

n=int(input("Enter the number of times to be printed "))
Oddseries(n)