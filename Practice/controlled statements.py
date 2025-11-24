lang=['python','java','c','c++','mysql','ds','flask','javascript']
for i in lang:
    print(i)
for i in enumerate(lang):
    print(i,i[0],i[1])

    
lang={'python','java','c','c++','mysql','ds','flask','javascript'}
for i in lang:
    print(i)


lang=('python','java','c','c++','mysql','ds','flask','javascript')
for i in lang:
    print(i)
for i in enumerate(lang):
    print(i,i[0],i[1])



lang={1:'python',2:'java',3:'c',4:'c++'}
for i in lang:
    print(f'key-{i} value-{lang[i]}')
for i in enumerate(lang):
    print(f'index-{i[0]} key-{i[1]} value-{lang[i[1]]}')


lang='python programming'
for i in lang:
    print(f'{i}')
for i in enumerate(lang):
    print(f'index-{i[0]} value-{i[1]}')

'''
for var in seq:
    #stms
for var in  enumerate(seq):
    #stms
for i in range(start,end+1,step):
    #stms
for i in range(len(seq)):
    #stms
seq:list,tuple,set,dict,str,range()
'''
num=int(input("Enter the number:"))
for i in range(1,21):
    print(f'{num}*{i}={num*i}')

l=['laptop','charger','phone','keyboard']
for i in range(len(l)):
    print(i,l[i])
