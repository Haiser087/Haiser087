def compute_lcm(a,b):

    if a>b:
     greater = a
    else:
     greater = b

     while(True):
       if(greater%a==0)and(greater%b==0):              # Does not works , needs correction
         lcm = greater
         break
       greater +=1

       return lcm
     
num1 = 6
num2 = 3

print("LCM is", compute_lcm(num1,num2))