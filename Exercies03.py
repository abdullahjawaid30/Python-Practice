import random 

computer=-random.choice([-1,0,1])

you=input("Enter Your Choice: S,W,G")

youDict={
    "s": 1,
    "w": -1,
    "g": 0
}
reverseDict={
    1: "Snake",
   -1: "Water",
    0: "Gun"
}
youNum=youDict[you]

print(f"you Chose {reverseDict[youNum]} \n Computer Chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")
    
else:
    if(computer == -1 and youNum == 1):
        print("You Win!")  
    elif(computer==-1 and youNum==0):
        print("You Lose!") 
        
    elif(computer==1 and youNum==1):
        print("You Lose!")  
    elif(computer==1 and youNum==0):
        print("You Win!") 
        
    elif(computer==0 and youNum==-1):
        print("You Win!")  
    elif(computer==0 and youNum==1):
        print("You Lose!")
        
    else:
        ("You Enter A Wrong Number")