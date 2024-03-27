print("<--Student Management System-->")
studentInfo = {}
#student add
while True:
    choice = input("What do you want to do? \n --Add Student \n --Update a Record \n --Show Record \n --Remove a Record \n --Delete Record \n --Exit \n")
    choice = choice.lower()
    if "add" in choice:
        name = input("Enter Student Name: ")
        studentInfo["Name"] = name
        age = input("Enter Student Age: ")
        studentInfo["Age"] = age
        id = input("Enter Student ID: ")
        studentInfo["ID"] = id
        course = input("Enter Student Course: ")
        studentInfo["Course"] = course
    elif "show" in choice:
        print(studentInfo)
    elif "delete" in choice:
        del studentInfo
        print("record deleted")
    elif "update" in choice:
        pop = input("what do you want to Chnage? \n --Name \n --ID \n --Age \n --Course \n")
        pop = pop.lower()
        if "name" in pop:
            name = input("Enter New Name: ")
            studentInfo["Name"] = name
        elif "age" in pop:
            age = input("Enter Student Age: ")
            studentInfo["Age"] = age
        elif "id" in pop:
            id = input("Enter Student ID: ")
            studentInfo["ID"] = id
        elif "course" in pop:
            course = input("Enter Student Course: ")
            studentInfo["Course"] = course
        else:
            print("Wrong input")
    elif "remove" in choice:
        pop = input("what do you want to remove? \n Name \n ID \n --Age \n --Course \n")
        pop = pop.lower()
        if "name" in pop:
            studentInfo.pop("Name")
        elif "age" in pop:
            studentInfo.pop("Age")
        elif "id" in pop:
            studentInfo.pop("ID")
        elif "course" in pop:
            studentInfo.pop("Course")
        else:
            print("Wrong input")
    elif "exit" in choice:
        print("Exiting the program")
        break
    else:
        print("wrong input")