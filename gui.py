import tkinter as tk
from tkinter import filedialog

def browse():
    folder = filedialog.askdirectory()
    output.delete(0, tk.END)
    output.insert(0, folder)

def build():
    print("Building EXE...")

def run():
    root = tk.Tk()
    root.title("Shiny Website To EXE")

    tk.Label(root, text="Website URL").pack()
    tk.Entry(root, width=50).pack()

    tk.Label(root, text="App Name").pack()
    tk.Entry(root, width=50).pack()

    tk.Label(root, text="Output Folder").pack()

    global output
    output = tk.Entry(root, width=50)
    output.pack()

    tk.Button(root, text="Browse", command=browse).pack()
    tk.Button(root, text="Build EXE", command=build).pack(pady=10)

    root.mainloop()
