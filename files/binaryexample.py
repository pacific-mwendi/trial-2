with open("image 4.jpg","rb") as f:
    data = f.read()
    print(type(data))

with open("image4.jpg","wb") as f :
   f.write(b"helllo")
    
    #writimgf numbers as binary

with open("numbers.bin", "wb") as f:
    data = bytes([10, 20, 30, 40])
    f.write(data)    