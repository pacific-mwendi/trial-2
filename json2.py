#importing module
import json

#creating data
data =[
{    "name":"pacific",
     "age" :18,
     "city" :"nairobi"
},
{    "name" :"ethan",
    "age"   : 17,
    "city"  : "kisumu" 
}]


with open("data.json","w") as file:
    json.dump(data,file)

with open("data.json","r") as reader:
    info = json.load(reader)
print(info[0]["city"])     

