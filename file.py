import random

# open a file

# Read From File

# file=open('file.txt')
# data=file.read()
# print(data)
# file.close()


# Write From File
# str="Hello This is writing in a new file"
# file=open("myTextFile.txt","w")
# file.write(str)
# file.close


# open a multiple file line 
# file=open("file.txt")
# lines = file.readlines()
# print(lines,type(lines))
# file.close()

# open a one  line
# file=open("file.txt")
# line =file.readline()
# while(line != ""):
#     print(line)
    
# file.close()


# file=open("file/poem.txt")
# content=file.read()
# if("twinkle" in content):
#     print("twinkle is in the file")
# else:
#     print("twinkle is not in the file")

# file.close()


# def game():
#     print("you are playing the game...")
#     score=random.randint(1,62)
#     #Fetch the highscore
#     with open("file/highScore.txt") as file:
#         highScore = file.read()
#         if(highScore != ""):
#             highScore = int(highScore)
#         else:
#             highScore = 0

#     print(f"Your Score:{score}")
#     if(score>highScore):
#        with open("file/highScore.txt","w") as file:
#            file.write(str(score))
#     return score

# game()



# def generateTable(n):
#     table=""
#     for i in range(1,11):
#         table+=f"{i} * {n} = {i*n}\n"
#     with open(f"file/tables/table_{n}.txt","w") as file:
#       file.write(table) 


# for i in range(2,21):
#    generateTable(i)



# word="Donkey"

# with open("file/file.txt","r") as file:
#     content =file.read()

# contentNew=content.replace(word,"#####")

# with open("file/file.txt","w") as file:
#     file.write(contentNew)



words=["Women","independent","not"]

with open("file/file.txt","r") as file:
    content =file.read()


for word in words:
   content=content.replace(word,"#" * len(word))

with open("file/file.txt","w") as file:
    file.write(content)