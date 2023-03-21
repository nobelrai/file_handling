import json


def password_required(func):
    def inner_func(*args, **kwargs):
        password = input("Enter the password ")
        with open("password.json", 'r') as fp:
            data = json.load(fp)
        if password == data['password']:
            print("Access Given")
            return func(*args, **kwargs)
        else:
            print("Permission Denied !!")
    return inner_func
