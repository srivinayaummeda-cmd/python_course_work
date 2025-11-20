amount=int(input("Enter the amount"))
actual_amount=amount
if amount>=10000:
    actual_amount=amount-amount*0.5
elif 8000<=amount<10000:
    actual_amount=amount-amount*0.3
elif 5000<=amount<8000:
    actual_amount=amount-amount*0.2
elif 2000<=amount<5000:
    actual_amount=amount-amount*0.05
print(f"Amount: {amount}\n After discount:{actual_amount}")



budjet=int(input("Enter the budjet:"))
if budjet>20000:
    print("Trip to Goa")
elif 15000<=budjet<20000:
    print("Go for Shopping")
elif 10000<=budjet<15000:
    print("Clubbing")
elif 5000<=budjet<10000:
     print("Go for cafe")
elif 2000<=budjet<5000:
    print("Go for movie")
elif 1000<=budjet<5000:
    print("Go for Temple")
elif 500<=budjet<1000:
    print("Go for Recharge")
elif 100<=budjet<500:
    print("Go for Biryani")
elif 50<=budjet<100:
    print("Go for Tea")
else:
     print("Go for sleep")

Products=['laptop','mouse','phone','keyboard','speaker']
stocks=[100,20,0,5,99]
print("*"*30)
print(Products)
print("*"*30)
network=True

if network:
    Product=input("Enter the Product:").strip()
    if Product in Products:
        index=Products.index(Product)
        if stocks[index]==0:
            print(f'{Product}-out of stock')
        elif 1<=stocks[index]<=10:
            print(f'{Product}-only few items left.Hurry Up')
        else:
            print(f'{Product}')
    else:
        print("Product not found")
else:
    print("checkout the internet")



data={
    'vinaya':{'python':99,'mysql':90,'flask':98},
    'divya':{'python':90,'mysql':70,'flask':78},
    'akshitha':{'python':69,'mysql':50,'flask':88}
    }
user=input("Enter the user:")
print(data[user])
avg=(data[user]['python']+data[user]['mysql']+data[user]['flask'])
if 80<=avg<=100:
    print(f'{user} got "A" grade.\nKeep it up')
elif 60<=avg<=80:
    print(f'{user} got "B" grade.\nGood,Need to improve')
elif 40<=avg<=60:
     print(f'{user} got "C" grade.\nAverage,practice well')
elif avg<40:
    print(f'{user} got Failed!!\nBring your parents')


