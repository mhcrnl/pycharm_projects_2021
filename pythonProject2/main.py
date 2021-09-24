#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

# Start coding here
class Biblioteca(tk.Frame):

    def __init__(self, parent, *args, **kargs):
        super().__init__(parent, *args, **kargs)

        self.titlu = tk.Label(self, text="Titlu: ")
        self.titlu_e = tk.Entry(self)

        self.autor = tk.Label(self, text="Autor:")
        self.autor_e = tk.Entry(self)

        self.editura= tk.Label(self, text="Editura:")
        self.editura_e = tk.Entry(self)

        self.an = tk.Label(self, text="An:")
        self.an_e = tk.Entry(self)

        self.save = tk.Button(self, text="Save")
        self.exit = tk.Button(self, text="Exit", command=self.quit)
        self.reset = tk.Button(self, text="Reset", command=self.reset)


        self.titlu.grid(row=0, column=0, sticky=tk.W)
        self.titlu_e.grid(row=0, column=1, sticky=tk.W)

        self.autor.grid(row=1, column=0, sticky=tk.W)
        self.autor_e.grid(row=1, column=1, sticky=tk.W)

        self.editura.grid(row=2, column=0, sticky=tk.W)
        self.editura_e.grid(row=2, column=1, sticky=tk.W)

        self.an.grid(row=3, column=0, sticky=tk.W)
        self.an_e.grid(row=3, column=1, sticky=tk.W)

        self.exit.grid(row=4, column=0, sticky=tk.W)
        self.reset.grid(row=4, column=1, sticky=tk.W)
        self.save.grid(row=4, column=2, sticky=tk.W)

        self.columnconfigure(1, weight=1)

    def reset(self):
        self.an_e.delete(0,tk.END)
        self.titlu_e.delete(0, tk.END)
        self.autor_e.delete(0, tk.END)
        self.editura_e.delete(0, tk.END)

class Application(tk.Tk):
    """Application root window"""
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.title("Biblioteca")
        self.geometry("400x400")

        Biblioteca(self).grid(sticky=(tk.E+tk.W+tk.N+tk.S))
        self.columnconfigure(0, weight=1)

if __name__ == "__main__":
    app = Application()
    app.mainloop()

