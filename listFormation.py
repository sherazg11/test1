itemList = []
while True:
    print("What do you want to do? \n Add \n Remove \n Show \n Exit")
    choice = input("Your Choice: ")
    if choice == "add":
        item = input("Add an item: ")
        itemList.append(item)
    elif choice == "remove":
        item = input("Remove from list: ")
        itemList.remove(item)
    elif choice == "exit":
            print("Exiting the program")
            break
    elif choice == "show":
            print("Your Current List is: \n", itemList)
    else:
          print("Invalid Input Try Again")