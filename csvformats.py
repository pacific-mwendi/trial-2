import csv

# Writing
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 20])

# Reading
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)