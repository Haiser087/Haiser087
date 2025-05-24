def main():

    x = int(input("Enter the numner"))
    if iseven(x):
        print("true")
    else:
            print("false")

def iseven(n):
    return n%2 == 0

main()