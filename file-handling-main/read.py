import json
from decorator import password_required
filename = "students.json"


@password_required
def read(id):
    with open(filename, 'r') as fp:
        students = json.load(fp)
    student = list(filter(lambda x: x['id']==id, students))
    print(student[0])
    cont = input("Do you want to continue? (y/n)")
    return True if cont.lower() == 'y' else False
