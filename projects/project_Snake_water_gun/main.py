import random

comp = random.choice([1,-1,0])

def game(comp,yourChoice):
    dict = {'s':1,'w':-1,'g':0}
    revdict = {1:'Snake', -1:'Water', 0:'Glass'}
    you = dict[yourChoice]
    print(f"you choose {revdict[you]} and computer choosed {revdict[comp]}")

    if(comp == yourChoice):
        print("its draw")
    else:
        if(comp==-1 and you == 1):
            print("you win")
        elif( comp==-1 and you == 0):
            print("you lose")
        elif(comp==1 and you == -1):
            print("you win")
        elif( comp==1 and you == 0):
            print("you lose")
        if(comp==0 and you == 1):
            print("you win")
        elif( comp==0 and you == -1):
            print("you lose")
        else:
            print("you entered something wrong")

    

i = - 1

while(i!=0):
    cont = int(input("1 for continue/ 0 for stop: "))
    if(cont == 1):
        yourChoice = input("Enter your choice(s/w/g): ")
        game(comp,yourChoice)
    else:
        i = cont
        
