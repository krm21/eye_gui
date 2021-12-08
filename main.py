import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import filedialog as fd

class MainWindow:
    def __init__(self, root):
        self.label = ttk.Label(root, text="dupa")
        self.label.pack(side=tk.LEFT)
        r = ttk.Frame(root)
        r.pack(side=tk.RIGHT)

        b1 = tk.Button(r, text="Open an image...", command=self.select_file)
        b1.grid(row=0, column=1)
        s1 = tk.Scale(r, from_=0, to=10, orient=tk.HORIZONTAL, length=300, label="blur")
        s1.grid(row=1, column=1)
        s2 = tk.Scale(r, from_=0, to=10, orient=tk.HORIZONTAL, length=300, label="contrast")
        s2.grid(row=2, column=1)
        s3 = tk.Scale(r, from_=0, to=10, orient=tk.HORIZONTAL, length=300, label="brightness")
        s3.grid(row=3, column=1)
        s4 = tk.Scale(r, from_=0, to=10, orient=tk.HORIZONTAL, length=300, label="lower sigma")
        s4.grid(row=4, column=1)
        s5 = tk.Scale(r, from_=0, to=10, orient=tk.HORIZONTAL, length=300, label="upper sigma")
        s5.grid(row=5, column=1)

    def select_file(self):
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.')

        self.pic = PhotoImage(file = self.filename)

        self.label.config(image=self.pic)
        

if __name__ == '__main__': 
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()