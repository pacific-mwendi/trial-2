import os

f = open("names.txt", "r") 

#print(f.read())
#print(f.read(3))  
#print(f.read(5))

print(f.readline())
print(f.readline())

for line in f :
    print(line)

f.close()    

try :
    f=open("name_list.txt","r")
except:
    print("file does not exist")    
finally:
    f.close()   

# a to represent append
# f = open("name_list.txt","a")
# f.write("pacific")
# f.close() 

#reading the new file
f = open("name_list.txt","r")
print(f.read())
f.close() 
 
 #write(overwrite)
f = open("context.txt","w")
f.write("all the data was deleted") 
f.close()

#reading the overwrite contents
f= open("context.txt","r")
print(f.read())
f.close()

#2 ways to create a file
#1.open a file for writing and vreates a file if it does not exist

f = open("car_list.txt","w")
f.close()

#2.to create a specified file but returns error if the file does not exist
if not os.path.exists("pacific.txt"):
  f = open("pacific.txt","x")
  f.close()

#deleting a file 
#avoiding an error if the file does not exist  

if os.path.exists("pacific.txt"):
   os.remove("pacific.txt")
else:
    print("the file does not exist")

with open("context.txt") as f:
    content = f.read() 

with open("names.txt") as f :
    f.write(content)  