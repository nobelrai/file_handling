from create import create
from read import read
from update import update
from delete import delete


def inquiry():
    selection = input("Welcome to Broadway. Choose C/R/U/D/E ")
    selection = selection.lower()

    def continue_or_not(c):
        inquiry() if c else print("Thank you see you again")

    if selection == 'c':
        cont = create()
        return continue_or_not(cont)
        # if cont:
        #     inquiry()
        # else:
        #     print("Thank You. See you again")
    elif selection == 'r':
        id = input("Enter the student ID ")
        cont = read(id)
        return continue_or_not(cont)
    elif selection == 'u':
        id = input("Enter the student ID ")
        to_change = input("What do you wish to update? (name, age, department) ")
        value = input(f"Give the new {to_change} ")
        cont = update(id, to_change, value)
        return continue_or_not(cont)

    elif selection == 'd':
        id = input("Enter the student ID ")
        cont = delete(id)
        return continue_or_not(cont)
    else:
        print("Thank You. See you again")


if __name__ == "__main__":
    inquiry()
