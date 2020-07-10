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


def input_data():
    name1 = name.get()
    quantity1 = quantity.get()
    datein1 = datein.get()
    if name1 == "":
        result1.set("Please enter an ID!")
    elif name1 in data:
        result1.set(name1+" is already in the system!")
    else:
        data[name1] = [quantity1, datein1]
        with open('inventory.txt', 'w', encoding='UTF-8-sig') as f:
            f.write(str(data))
        result1.set(name1+" is saved successfully.")


def disp_data():
    if len(listofbutton) > 0:
        for i in listofbutton:
            i.destroy()
    text = tk.Text(frame02)
    text.insert(tk.INSERT, "ID  \tQuantity  \tDate\n")
    for k in data:
        text.insert(tk.INSERT, "{}\t{}\t{}\n".format(k, data[k][0], data[k][1]))
    text.pack()
    listofbutton.append(text)

def edit_yes():
    result1.set("")
    ynbtn.destroy()
    data[name1][0] = quantity1
    data[name1][1] = datein1
    with open('inventory.txt', 'w', encoding='UTF-8-sig') as f:
        f.write(str(data))
    result1.set(name1+" is edited.")

def edit_data():
    global ynbtn, name1, quantity1, datein1
    name1 = name.get()
    quantity1 = quantity.get()
    print(type(quantity1))
    datein1 = datein.get()
    if name1 == "":
            result1.set("Please enter an ID!")
    elif not name1 in data:
        result1.set(name1 + " does not exist in the system.")
    else:
        newdata = "Are you sure you want to chane it to " + quantity1 + " on " + datein1 +"?"
        result1.set("Original data: "+ name1 + " has quantity of "+ data[name1][0]+" on " + data[name1][1] +".\n" + newdata)
        ynbtn = tk.Button(frame04, text="Yes", command=edit_yes)
        ynbtn.pack(pady=5)

def delete_yes():
    result1.set("")
    ynbtn.destroy()
    del data[name1]
    with open('inventory.txt', 'w', encoding='UTF-8-sig') as f:
        f.write(str(data))
    result1.set(name1+" is deleted.")

def delete_data():
    global name1, ynbtn
    name1 = name.get()
    if name1 == "":
        result1.set("Please enter an ID!")
    elif not name1 in data:
        result1.set(name1 + " does not exist in the system.".format(name1))
    else:
        result1.set("Are you sure you want to delete {}".format(name1))
        ynbtn = tk.Button(frame04, text="Yes", command=delete_yes)
        ynbtn.pack(pady=5)

def add_entry():
    result1.set("")
    if len(listofbutton) > 0:
        for i in listofbutton:
            i.destroy()
    label01 = tk.Label(frame02, text="Product ID:")
    entry_id = tk.Entry(frame02, textvariable=name)
    label02 = tk.Label(frame02, text="Quantity:")
    entry_q = tk.Entry(frame02, textvariable=quantity)
    label03 = tk.Label(frame02, text="Date(mm/dd/yyyy):")
    entry_date = tk.Entry(frame02, textvariable=datein)
    label01.grid(row=0, column=0, pady=5)
    entry_id.grid(row=0, column=1, pady=5)
    label02.grid(row=1, column=0, pady=5)
    entry_q.grid(row=1, column=1, pady=5)
    label03.grid(row=2, column=0, pady=5)
    entry_date.grid(row=2, column=1, pady=5)
    datago = tk.Button(frame03, text="Enter", command=input_data)
    datago.pack(pady=5)
    listofbutton.extend((label01, label02, label03, entry_date, entry_q, entry_id, datago))

def edit_entry():
    result1.set("")
    if len(listofbutton) > 0:
        for i in listofbutton:
            i.destroy()
    label01 = tk.Label(frame02, text="Product ID:")
    entry_id = tk.Entry(frame02, textvariable=name)
    label02 = tk.Label(frame02, text="Quantity:")
    entry_q = tk.Entry(frame02, textvariable=quantity)
    label03 = tk.Label(frame02, text="Date(mm/dd/yyyy):")
    entry_date = tk.Entry(frame02, textvariable=datein)
    label01.grid(row=0, column=0, pady=5)
    entry_id.grid(row=0, column=1, pady=5)
    label02.grid(row=1, column=0, pady=5)
    entry_q.grid(row=1, column=1, pady=5)
    label03.grid(row=2, column=0, pady=5)
    entry_date.grid(row=2, column=1, pady=5)
    datago = tk.Button(frame03, text="Enter", command=edit_data)
    datago.pack(pady=5)
    listofbutton.extend((label01, label02, label03, entry_date, entry_q, entry_id, datago))

def delete_entry():
    result1.set("")
    if len(listofbutton) > 0:
        for i in listofbutton:
            i.destroy()
    label01 = tk.Label(frame02, text="Product ID:")
    entry_id = tk.Entry(frame02, textvariable=name)
    label01.grid(row=0, column=0, pady=5)
    entry_id.grid(row=0, column=1, pady=5)
    datago = tk.Button(frame03, text="Enter", command=delete_data)
    datago.pack(pady=5)
    listofbutton.extend((label01, entry_id, datago))

###Main program starts here###

import os, ast
import tkinter as tk

listofbutton=[]
data = read_data()
win = tk.Tk()
win.geometry("640x400")
win.title("Inventory Management System")
name = tk.StringVar()
quantity = tk.StringVar()
datein = tk.StringVar()
result1 = tk.StringVar()

label_title = tk.Label(win, text="\nInventory Management System", font=("Arial", 20))
label_title.pack()

frame01 = tk.Frame(win)
frame01.pack()

btn1 = tk.Button(frame01, text="Add inventory items", width=20, command=add_entry)
btn1.grid(row=0, column=0, pady = 5)
btn2 = tk.Button(frame01, text="Show all inventory items", width=20, command=disp_data)
btn2.grid(row=1, column=0, pady = 5)
btn3 = tk.Button(frame01, text="Edit inventory items", width=20, command=edit_entry)
btn3.grid(row=2, column=0, pady = 5)
btn4 = tk.Button(frame01, text="Delete inventory items", width=20, command=delete_entry)
btn4.grid(row=3, column=0, pady = 5)

frame02 = tk.Frame(win)
frame02.pack()
frame03 = tk.Frame(win)
frame03.pack()
frame04 = tk.Frame(win)
frame04.pack()

message = tk.Label(frame04, textvariable=result1, fg="red", font = ("Arial", 16))
message.pack(pady=5)

win.mainloop()