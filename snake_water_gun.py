import random
def gameWin(comp , you):
    if comp == you:
        return None
    elif comp =='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False


print("Comp Turn: Snake(s)  Water(w)  or Gun(g) ?")
r=random.randint(1,3)

if r == 1:
    comp = 's'
elif r == 2:
    comp = 'w'
elif r == 3:
    comp = 'g'
    
you=input("\n your turn: snake(s) , water(w) , gun(g) ?")

a=gameWin(comp,you)
print(f"\n computer choose :{comp}")
print(f"\n you choose :{you}")
if a==None:
    print("tie..")
if a:
    print("you win...!")
else:
    print("you loose")

    