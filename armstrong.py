import math

num = 145
length = len(str(num))

while num != 0 :
     digit = num % 10
     sum += math.pow(digit , length)
     num  //= 10

     if num == sum :
         print("The number is armstrong")
         else :

     
     
