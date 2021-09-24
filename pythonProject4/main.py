# This is a sample Python script.
import tkinter as tk

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def show_entry_fields():
    print("Nume: %s\nPrenume: %s" %(e1.get(), e2.get()))

def sterge():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

master = tk.Tk()

tk.Label(master, text="Nume").grid(row=0)
tk.Label(master, text="Prenume").grid(row=1)

e1=tk.Entry(master)
e2=tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text="Inchide", command=master.quit).grid(row=3,
                                                            column=0,
                                                            sticky=tk.W,
                                                            pady=4)
tk.Button(master, text="Afiseaza", command=show_entry_fields).grid(row=3,
                                                                   column=1,
                                                                   sticky=tk.W,
                                                                   pady=4)
tk.Button(master, text="Sterge", command=sterge).grid( row=3, column=2,
                                                       sticky=tk.W,
                                                       pady=4)
tk.mainloop()
""" 

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""