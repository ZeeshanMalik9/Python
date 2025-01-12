n = int(input("enter a number: "))

def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
    
print(sum(n))