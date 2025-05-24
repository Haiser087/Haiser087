a = int(input("What's the number user wants to see factorial of"))

factorial = 1 

for i in range(1,  a+1):
 factorial *= i 

print(f"the factorial of the {a} is {factorial}")