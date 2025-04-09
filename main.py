import tkinter as tk
from Item import Item

#create window
root = tk.Tk()

#create item and display it
sampleItem = Item("Sword", "A tool used for slicing up villians", None)

itemStr = "Item 1: " + sampleItem.getName() 

tk.Label(root, text=itemStr).pack()
tk.Label(root, text="Description: " + sampleItem.getDesc()).pack()

root.mainloop()