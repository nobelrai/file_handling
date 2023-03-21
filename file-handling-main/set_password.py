import json
password = input("Set the password ")
data = {'password': password}

with open("password.json", 'w') as fp:
    json.dump(data, fp, indent=2)

print("Your password set successfully !!")