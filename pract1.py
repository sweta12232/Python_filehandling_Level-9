with open("pratice.txt", "r") as f:
   data =  f.read()
new_data = data.replace("Java", "Python")
print(new_data)