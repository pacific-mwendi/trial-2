import csv 
#with open("data.csv","r") as file:
   #reader = csv.reader(file)
   #for row in reader:
      #print(row)
#with open("data.csv","w") as files:
   #files.write("eric,18,male")

#with open("data.csv","r+") as docs:
   
 #docs.write("mark,18,male")  
 #docs.read()




with open("data.csv", "r+") as file:
    reader = csv.reader(file)
    
    # Read existing content
    for row in reader:
        print(row)
    
    # Move cursor to end before writing
    file.seek(0, 2)
    
    writer = csv.writer(file)
    writer.writerow(["pacific", 18, "male"])