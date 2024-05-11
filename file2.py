# to read the speficic character of file

f = open("sample.txt", "r")
data = f.read(1)
print(data)

f.close()