'''
import math
print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.pow(2,5))
print(math.ceil(12.3))
print(math.ceil(12.23))
print(math.floor(12.3))
print(math.floor(12.3))
print(math.fabs(-12.3))
print(math.factorial(7))
print(math.gcd(50,100))
print(math.sin(30))
print(math.cos(45))
print(math.tan(60))
print(math.log(2,2))
print(math.degrees(30))
print(math.radians(30))



from collections import Counter,defaultdict,deque
s='python'
s1='vinaya is regular to class divya also regular'
l=[1,2,34,5,45,6]
t=(1,2,3,4,4,5,6)
set={1,2,3,4,5,6}
print(Counter(s))
print(Counter(s1.split()))
print(Counter(l))
print(Counter(t))
print(Counter(set))




from collections import Counter,defaultdict,deque
d=defaultdict(int)
s='python programming'
for i in s:
    d[i]+=1
print(d)   
        



from collections import Counter,defaultdict,deque
d=deque([])
d.append(10)
d.append(20)
d.append(30)
d.popleft()
d.popleft()
d.append(80)
d.append(80)
print(d)
q=deque([])
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.pop()
q.pop()
q.appendleft(80)
q.appendleft(90)
print(q)
'''
from itertools import combinations,permutations
s='abc'
print(list(combinations(s,2)))
print(list(permutations(s,2)))   

























