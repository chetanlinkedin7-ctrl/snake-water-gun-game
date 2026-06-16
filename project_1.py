
import random

computer = random.choice([1,0,-1])

dicgame ={

    "snake":1,
    "water" :0,
    "GUN":-1
}
youstr = input("enter your Weapons : ")
you = dicgame[youstr]
print(you)

revdic = {1:"snake",0:"water",-1:"GUN"}
print(f"you chose {revdic[you]},\n computer choose {revdic[computer]}")

if(computer==you):
    print("its is draw ")
else:
    if(computer==1 and you==0):
       print("YOU LOSE!")

    elif(computer==0 and you==1):
       print("YOU WIN!")   

    elif(computer==0 and you==-1):
       print("YOU LOSE!") 

    elif(computer==-1 and you==0):
       print("YOU WIN!")

    elif(computer==-1 and you==1):
        print("YOU LOSE")

    elif(computer==1 and you==-1):
        print("YOU WIN!")

    else:
        print("SOMETHING IS WRONG!!")


