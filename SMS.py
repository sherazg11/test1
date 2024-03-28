print("<--Student Management System-->")

studentInfo = {}


while True:
    
    choice = input("What do you want to do? \n --Add Student \n --Update a Record \n --Show Record \n --Delete Record \n --Exit \n")
    choice = choice.lower()

    if "add" in choice:
    
        id = input("Enter Student ID: ")
        stdinfo = {}
        name = input("Enter Student Name: ")
        stdinfo["Name"] = name
        age = input("Enter Student Age: ")
        stdinfo["Age"] = age
        course = input("Enter Student Course: ")
        stdinfo["Course"] = course
        studentInfo[id] = stdinfo
    
    elif "show" in choice:
    
        print(studentInfo)
    
    elif "delete" in choice:
    
        print("Which Record You want to Delete(using ID)? ")
        id = input("Enter Student ID: ")
    
        if id in studentInfo:
            del studentInfo[id]
        else:
            print("Invalid ID")
    
    elif "update" in choice:
    
        print("Which Record You want to Delete(using ID)? ")
        id = input("Enter Student ID: ")
    
        if id in studentInfo:
            pop = input("what do you want to Chnage? \n --Name \n --Age \n --Course \n")
            pop = pop.lower()
    
            if "name" in pop:
                name = input("Ent0er New Name: ")
                stdinfo["Name"] = name
    
            elif "age" in pop:
                age = input("Enter Student Age: ")
                stdinfo["Age"] = age
    
            elif "course" in pop:
                course = input("Enter Student Course: ")
                stdinfo["Course"] = course
    
            else:
                print("Wrong input")
        else:
            print("Invalid ID")
    
    elif "exit" in choice:
    
        print("Exiting the program")
        break
    
    else:
        print("wrong input")