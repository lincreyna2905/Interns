from tkinter import *
from tkinter import ttk


item = []
quantity = []
price = []

root = Tk()
root.title("Grocery List")
root.geometry("720x720")

content = StringVar()

tree= ttk.Treeview(column=("c1", "c2", "c3"), show='headings', height=8)
tree.column("# 1", anchor=W)
tree.heading("# 1", text="Items")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Quantity")
tree.column("# 3", anchor=E)
tree.heading("# 3", text="Price")

tree.pack()


entry1 = Entry(root)
entry1.pack()
entry2 = Entry(root)
entry2.pack()
entry3 = Entry(root)
entry3.pack()


label1 = Label(root, text="Item: ", fg="black")
label1.place(x=260,y=188)

label2 = Label(root, text="Quantity: ", fg = "black")
label2.place(x=238, y=205)

label3 = Label(root, text="price: ", fg = "black")
label3.place(x=255, y=223)


def getInput():
    tree.insert()
        
    
def delete():
    selectedItem = tree.curselection()
    for index in selectedItem:
        tree.delete(index)
    

addButton = Button(root, command=getInput, text="Add")
addButton.pack()

deleteButton = Button(root, command=delete, text="Delete")
deleteButton.pack()




root.mainloop()


