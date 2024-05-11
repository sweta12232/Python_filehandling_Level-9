#to print first line of the text
f = open("sample.txt", "r") #'n so that there is space int
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()