def fiboIter(n):
    prevNumber = 0
    currNumber = 1
    for i in range(1,n):
         prevPrevNumber = prevNumber
         prevNumber = currNumber
         currNumber = prevNumber + prevPrevNumber
    return currNumber

def fiboRecur(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)

 

if __name__ == "__main__":
    
    a = int(input("Enter a number"))

print(f"Using recursion the answer of fib({a}) is {fiboRecur(a)}")
print(f"Using iteration the answer of fib({a}) is {fiboIter(a)}")

