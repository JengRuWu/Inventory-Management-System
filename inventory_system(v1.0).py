def read_data():
    if not os.path.isfile('inventory.txt'):
        open('inventory.txt', 'w', encoding='UTF-8-sig')
        return dict()
    else:
        with open('inventory.txt','r', encoding='UTF-8-sig') as f:
            filedata = f.read()
            if filedata != "":
                inventory_data = ast.literal_eval(filedata)
                return inventory_data
            else: return dict()


def menu():
    print("Inventory Management System")
    print("---------------------------")
    print("1. Add inventory items")
    print("2. Show all inventory items")
    print("3. Edit inventory items")
    print("4. Delete inventory items")
    print("0. Leave the system")
    print("---------------------------")


def input_data():
    while True:
        name = input("Please enter product ID to input (Press Enter to return to main menu):")
        if name == "" : break
        if name in data:
            print("This product is already in the system!")
            continue
        quantity = input("Please enter the quantity:")
        datein = input("Please enter the date (yyyy/mm/dd):")
        data[name] = [quantity,datein]
        with open('inventory.txt', 'w', encoding='UTF-8-sig') as f:
            f.write(str(data))
        print("Inventory item is saved.")


def disp_data():
    print("ID\tQuantity\tDate")
    print("--------------------------")
    for k in data:
        print("{}\t{}\t{}".format(k, data[k][0], data[k][1]))
    input("Press any button to return to menu.")


def edit_data():
    while True:
        name = input("Please enter product ID to edit (Press Enter to return to main menu):")
        if name == "":
            break
        if not name in data:
            print("{} does not exist in the system.".format(name))
            continue
        print("{} has quantity of {} on {}".format(name, data[name][0], data[name][1]))
        quantity = input("Please input new quantity:")
        indate = input("Please input new date:")
        data[name][0] = quantity
        data[name][1] = indate
        with open('inventory.txt', 'w', encoding='UTF-8-sig') as f:
            f.write(str(data))
        print("Inventory item is saved.")


def delete_data():
    while True:
        name = input("Please enter product ID to delete (Press Enter to return to main menu):")
        if name == "":
            break
        if not name in data:
            print("{} does not exist in the system.".format(name))
            continue
        print("Are you sure you want to delete {}".format(name))
        yn = input("Y/N")
        if yn == "Y" or yn == "y":
            del data[name]
            with open('inventory.txt', 'w', encoding='UTF-8-sig') as f:
                f.write(str(data))
            print("Inventory item is deleted.")


###Main program starts here###

import os, ast

data = read_data()

while True:
    menu()
    choice = int(input("What would you like to do?"))
    if choice == 1:
        input_data()
    elif choice == 2:
        disp_data()
    elif choice == 3:
        edit_data()
    elif choice == 4:
        delete_data()
    elif choice == 0:
        break
    else: print("Please enter a valid number.")

print("You have left the inventory management system")
