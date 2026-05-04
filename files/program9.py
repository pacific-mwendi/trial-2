with open("empty.txt","r") as file:
    content = file.read()

if content == "" :
    print("file empty")
else:
    print("file  not empty")        