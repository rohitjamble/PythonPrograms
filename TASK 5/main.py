#PRG--01

# person=[{"Name":"Rohit","age":27},
#         {"Name":"Amit","age":20},
#         {"Name":"Mahesh","age":16},
#         {"Name":"Suresh","age":14}    
#         ]
# Under_age=list(filter(lambda data:data["age"]<=18,person))
# print(Under_age)
# names=list(map(lambda data:data["Name"],Under_age))
# print(names)

# PRG--02
# from functools import reduce
# num=[5,10,12,15,20]
# result = reduce(lambda a,b:a*b,num )
# print(result)

#PRG -03
# list1=[1,2,3,4,5,7,8,10,11]
# even_no=lambda x:x%2==0
# list_comp=[x**2 for x in list1 if (even_no)(x)]
# print(list_comp)

#prg-04
# str="2608"
# res=lambda x:x.isdigit()
# print(res(str))

#prg--05
from datetime import *
date=datetime(2000,12,26)
res=lambda x:(x.year,x.month,x.day)
print(res(date))

#prg -06
n=10
a=0
b=1
res=lambda x,y:x+y
print(res(a,b))