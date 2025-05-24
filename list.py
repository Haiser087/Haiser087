Fruits = ["apple","bananan","cherry"]
Fruits.append("mango")
print(Fruits)

tuple = ("apple", "banana", "cherry")
tupletolist = list(tuple)
tupletolist.append("Mango")
print(tupletolist)


# as tuple dont have function like appehnd and remove , we can just convert tuple to list and then re convert it to list 

tuple = ("python","programming","1st year")
for i in tuple:
    print(i)