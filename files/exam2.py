with open("student.txt","a") as file:
 file.write("\ndavid")    

with open("student.txt","r") as file:
 print(file.read())