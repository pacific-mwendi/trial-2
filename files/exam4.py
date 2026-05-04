total = 0
count = 0

with open("numbers.txt","r") as file:
 for line in file:
    num = int(line.strip())
    total += num
    count += 1

average = total/count if count != 0 else 0

print("sum",total)
print("average",average)




