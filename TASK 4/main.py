#Prg-01
Num=[10,501,22,37,100,999,87,351]
even_no=[]
odd_no=[]
for i in Num:
    if i % 2==0:
        even_no.append(i)
    else:
        odd_no.append(i)    
print(even_no)
print(odd_no)        

#PRG-02
Num=[10,501,22,37,100,999,87,351]
Prime_no=[]
count=0
for i in Num:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        Prime_no.append(i)
        count+=1
print(Prime_no)            

 #PRG-04(sum of 1st and last digit)
Num=810589
digit=str(Num)
first=int(digit[0])
last=int(digit[-1])
print(f"sum of 1st and last digit is {first+last}")

#
Num=810589
last = Num%10
while Num > 10:
    Num = Num//10
first = Num
print(first+last)    

#PRG-05 
for one in range(11):
    for two in range(6):
        for five in range(3):
            for ten in range(2):
                sum=one*1+two*2+five*5+ten*10
                if sum==10:
                    print(one,two,five,ten)

#PRG-06
l1=[2,3,4,1,1,5,6,7,8,10]
l2=[1,2,3,4,5,6,7,8,9]
l3=[8,7,7,6,5,1,2,3]
duplicates=[]
for i in l1:
    if i in l2 and  i in l3:
        duplicates.append(i)
print(duplicates)        

#PRG-07
l1=[2,3,4,5,6,4,3,1,2]
for i in l1:
    if l1.count(i)==1:
        break
print(i)

#PRG-08
sorted_list=[2,4,6,8,10,12]
minimum=sorted_list[0]
for i in sorted_list:
    if i < minimum:
        minimum = i
print(minimum)
#or
print(min(sorted_list))

#PRG=9
nums=[10,20,30,9]
value=59
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k] == value:
                print(nums[i],nums[j],nums[k])

#PRG--10
nums=[4,2,-3,1,6]
for i in range(len(nums)):
    total=0
    for j in range(i,len(nums)):
        total+=nums[j]
        if total ==0:
            print("Success")                

