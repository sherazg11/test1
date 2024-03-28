print("<--Student Management System-->")

studentInfo = {}

def add():

    stdinfo = {}


    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")
    
    stdinfo["Name"] = name
    stdinfo["Age"] = age
    stdinfo["Course"] = course
    
    studentInfo[id] = stdinfo

def delete():
    print("Which Record You want to Delete(using ID)? ")
    id = input("Enter Student ID: ")
    
    if id in studentInfo:
        del studentInfo[id]
    else:
        print("Invalid ID")

def update():
    print("Which Record You want to Delete(using ID)? ")
    id = input("Enter Student ID: ")
    if id in studentInfo:
        pop = input("what do you want to Chnage? \n --Name \n --Age \n --Course \n")
        pop = pop.lower()
        if "name" in pop:
            name = input("Enter New Name: ")
            studentInfo[id]["Name"] = name
    
        elif "age" in pop:
            age = input("Enter Student Age: ")
            studentInfo[id]["Age"] = age
    
        elif "course" in pop:
            course = input("Enter Student Course: ")
            studentInfo[id]["Course"] = course
    
        else:
            print("Wrong input")
    else:
        print("Invalid ID")

while True:
    
    choice = input("What do you want to do? \n --Add Student \n --Update a Record \n --Show Record \n --Delete Record \n --Exit \n")
    choice = choice.lower()

    if "add" in choice:        
        add()
    
    elif "show" in choice:
    
        print(studentInfo)
    
    elif "delete" in choice:

        delete()

    elif "update" in choice:
    
        update()
        
    
    elif "exit" in choice:
    
        print("Exiting the program")
        break
    
    else:
        print("wrong input")