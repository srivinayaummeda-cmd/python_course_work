def reels(data):
    for i in data:
        yield i
data=['1..100','100..200','200..300','300..400','400..500','500..600']
scroll=reels(data)
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''
while True:
    ch=input("[S]croll or [B]ack:").lower()
    if ch=='s':
        
'''
