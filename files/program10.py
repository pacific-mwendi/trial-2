with open("empty.txt", "r") as file:
    content = file.read()
    if content == "":
        print("File is empty")
    else:
        print("File is not empty")