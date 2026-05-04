with open("source.txt","r") as sc:
    transfer = sc.read()
with open("destination.txt","w")  as des:
    des.write(transfer)    