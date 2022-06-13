import random

def swg(comp,mine):
    if(comp==mine):
        return None
    if(comp=='s' and mine=='g'):
        return True
    elif(comp=='g' and mine=='w'):
        return True
    elif(comp=='w' and mine=='s'):
        return True
    else:
        return False


choice = ('s','w','g')
mine = input("Choose either 's' for snake, 'g' for gun or 'w for water : ")
comp = random.randint(0,2)
comp=choice[comp]

win = swg(comp,mine)

print(f"You chose {mine} and the computer chose {comp}")

if win is None:
    print("Match Drawn")
if win:
    print("You Won the match!!")
else:
    print("You Lose")