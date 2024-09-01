from tkinter import *
from tkinter import ttk

root = Tk()

# Create the Notebook
frm = ttk.Notebook(root)
frm.grid(row=0, column=0)

# Create frames for each tab
tab1 = Frame(frm)
tab2 = Frame(frm)

# Add the tabs to the Notebook
frm.add(tab1, text="Tab 1")
frm.add(tab2, text="Tab 2")

# Tab 1 Widgets
ttk.Label(tab1, text="Hello World!").grid(column=0, row=0, padx=10, pady=10)
ttk.Button(tab1, text="Quit", command=root.destroy).grid(column=1, row=0, padx=10, pady=10)



root.mainloop()
