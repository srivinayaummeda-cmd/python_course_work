import random
p1=input("Enter the player-1:")
p2=input("Enter the player-2:")
winnig_point=100
p1_sc=0
p2_sc=0

while p1_sc<100 and p2_sc<100:
    p1_st=input("you want to continue the game (y) or (n):")
    if p1_st=='y':
        p1_dice=random.randint(1,6)
        print(f"{p1}:your dice score:{p1_dice}")
        p1_sc+=p1_dice
        print(f"{p1}:your total score:{p1_sc}")
    else:
        print(f'congrates!!!\n{p1} you win the game')
        break
    p2_st=input("you want to continue the game (y) or (n):")
    if p2_st=='y':
        p2_dice=random.randint(1,6)
        print(f"{p2}:your dice score:{p2_dice}")
        p2_sc+=p2_dice
        print(f"{p2}:your total score:{p2_sc}")
    else:
        print(f'congrates!!!\n{p2} you win the game')    
        break
