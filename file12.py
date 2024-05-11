#Deleting a file
#using the os module
# import os
# os.remove("data.txt")

with open("pratice.txt", "w") as f:
    f.write("Hi everyone")
    f.write("I am learning file handling in Java\n")
    f.write("I like programming in Java\n")