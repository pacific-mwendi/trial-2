f = open("context.txt","r")
#print(f.read())
#print(f.read(3))
#print(f.readline())

#to loop through and print every line
for line in f:
    print(line)
f.close()    

#openimg a file that we do not have using try,except and finally if the file we want exists it will just open the file without showing an error 

try:
    f = open("plane.txt",)
    print(f.read)
except:
    print("the file does not exist")    
finally:
    f.close()

#create a file hat does not exist using append
f = open("context.txt","a")
f.write("   pacific")
f.close()

#readimg the file we just created
f=open("context.txt","r")
print(f.read())
f.close

#overwriting a file
f = open("context.txt","w")
f.write("i deleted all the content")
f.close()

#reading the overwritten content
f = open("context.txt")
print(f.read())
f.close()

