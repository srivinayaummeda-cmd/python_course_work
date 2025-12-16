
import math
circle_geometry=lambda r: (round(math.pi*r*r,2),round(2*math.pi*r,2))

print(circle_geometry(7))
print(circle_geometry(2.5))

import random
def pick_random_team(members,team_size):
    print(random.choices(members,k=team_size))
pick_random_team(['Alice','bob','charlie','david'],2)
pick_random_team(['A','b','c','d'],3)

temp=[36,42,39,45,41]
res=list(filter(lambda i:i>40,temp))
print(res)


def is_prime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
            break
    if c==0:
       return True
    else:
        return False
n=int(input("enter the number:"))
print(is_prime(n))


def reverse_number(n):
    if n<=0:
        return
    print(n%10,end='')
    reverse_number(n//10)


reverse_number(1234)
reverse_number(450)

inp=['cat','car','bat','apple']
ch='c'
res=list(filter(lambda i: i.startswith(ch),inp))
print(res)

#string_utils.py
def is_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
def capitalize_words(text):
    return text.capitalize()
#main.py
#from string_utils import is_palindrome,capitalize_words
print(is_palindrome("madam"))
print(capitalize_words("hello world"))

words=['Apple','apple','Banana','banana','Cherry']
res=set(map(lambda i:i.lower(),words))
print(res)



def countdown(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
c=countdown(n)
for i in range(n+1):
    print(next(c))



def nested_sum(n):
    for i in n:
        if type(i)=="<class 'list'>":
            nested_sum(i)
        else:
            print(i)
nested_sum([[1,2],[3,[4,5]]])      
