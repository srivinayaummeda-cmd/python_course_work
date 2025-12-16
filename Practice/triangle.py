
a,b,c=tuple(map(int,input().split()))

'''
if a==b and a==c and b==c:
    print("equi")
elif a!=b and b!=c and a!=c:
    print("sca")
else:
    print("iso")


ch=input()
vol='aeiouAEIOU'
if ch in vol:
    print("vol")
elif ch.isalpha():
    print("cons")
elif ch.isdigit():
    print("dig")
else:
    print("spl")


units=int(input())
charge=0
if units<=100:
    charge=units*1
elif 100<units<=200:
    charge=100+(units-100)*2
else:
    charge=300+(units-200)*3
print(charge)


num=input()
res=0
l=len(num)
for i in num:
    res+=int(i)**l
if res==num:
    print("arm")
else:
    ("not arm")
'''

age=int(input())
price=100
fare=0
if age<s:
    fare=0
elif 5<=age<=18:
    fare=price-fare*0.5
elif age>60:
    fare=price-fare*0.3

