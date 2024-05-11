f = open("sample.txt", "r+")
f.write("Hello")
print(f.read())
f.close()