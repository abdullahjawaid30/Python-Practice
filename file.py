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
file=open("file.txt")
line =file.readline()
while(line != ""):
    print(line)
    
file.close()



