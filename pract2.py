def word_finder():
    word = "learning"
    with open("pratice.txt", "r")as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

def line_cheker():
    word = "learning"
    data = True
    lineNum = 1
    with open("pratice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(lineNum)
                return 
                lineNum += 1


        return -1


line_cheker()
