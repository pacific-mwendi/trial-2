import json

user = [{
    "name": "Brian",
    "age": 22,
    "city": "Nairobi"
},
{
    "name": "pacific",
    "age": 18,
    "city":"nairobi"
}]

with open("user.json", "w") as f:
    json.dump(user, f)



with open("user.json", "r") as f:
    user = json.load(f)
print(user[0]["name"])    
  