#import pandas as pd

#df = pd.DataFrame() 
#print(df)

#lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
#df = pd.DataFrame(lst) 
#print(df)


import pandas as pd

print("Pandas version:", pd.__version__)

b = [1,2,3,4,6,7,83]

ser23 =pd.Series(b) #creating a series with default index

print(ser23)
print(ser23[0])

a = [1,2,3,4,5,6,7,8,9,10]  #creating a sereis with a index of my own 

ser21 = pd.Series(a , index = ['a','b','c','d','e','f','g','h','i','j'])

#print(ser21)
print(ser21['g'])

data1 = { "Name" : [1234 , 4567, 3456] 
        , "Age" : ["ER", "IC",  "DF"]}

ef = pd.DataFrame(data1) 

print(ef)
print(ef['Name'])


data =  { "Part to excercise" : ["Chest", "Back", "Legs", "Shoulders", "Arms"]
         , "Exercise" : ["Bench Press", "Pull Up", "Squats", "Shoulder Press", "Bicep Curl"]
        , "Reps" : [10, 8, 12, 10, 15]
        , "Sets" : [3, 4, 3, 4, 3]}

df = pd.DataFrame(data , index = ['day1', 'day2', 'day3', 'day4', 'day5'])
print(df)