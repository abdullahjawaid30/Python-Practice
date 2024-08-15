import random 

number=random.randint(1,100)
attempt=-12

guesses=0

while(attempt != number):
    attempt=int(input("Guess the number :"))
    if(attempt>number):
        print("Lower number please!")
        guesses +=1
    elif(attempt<number):
         print("Higher number please!")
         guesses +=1
    

print(f"you have guessed the number{number} correctly in {guesses} attempt")     