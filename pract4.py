count = 0
with open("number.txt", "r") as f:
    data = f.read()
    print(data)

num = data.split(",")
for i in num:
    if(int(i)% 2 == 0):
        count += 1
        print(i)
print(f'The total number of even number is {count}')