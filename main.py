import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import filedialog as fd

import PIL
from PIL import Image
from filter import bacon

class MainWindow:
    def __init__(self, root):
        self.label = ttk.Label(root, text="dupa")
        self.label.pack(side=tk.LEFT)
        r = ttk.Frame(root)
        r.config(padding=(10, 10, 10, 10))
        r.pack(side=tk.RIGHT)

        self.b1 = tk.Button(r, text="Open an image...", command=self.select_file)
        self.b1.grid(row=0, column=1)
        self.s1 = tk.Scale(r, from_=0, to=20, orient=tk.HORIZONTAL, length=300, label="blur", command=lambda x: self.handle_slide())
        self.s1.grid(row=1, column=1)
        self.s1.set(1)
        self.s2 = tk.Scale(r, from_=0, to=20, orient=tk.HORIZONTAL, length=300, label="contrast", command=lambda x: self.handle_slide())
        self.s2.grid(row=2, column=1)
        self.s2.set(1)
        self.s3 = tk.Scale(r, from_=0, to=5, orient=tk.HORIZONTAL, length=300, label="brightness", command=lambda x: self.handle_slide())
        self.s3.grid(row=3, column=1)
        self.s3.set(1)
        self.s4 = tk.Scale(r, from_=0, to=30, orient=tk.HORIZONTAL, length=300, label="lower sigma", command=lambda x: self.handle_slide())
        self.s4.set(2)
        self.s4.grid(row=4, column=1)
        self.s5 = tk.Scale(r, from_=0, to=30, orient=tk.HORIZONTAL, length=300, label="upper sigma", command=lambda x: self.handle_slide())
        self.s5.set(20)
        self.s5.grid(row=5, column=1)

    def select_file(self):
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.')

        self.image = Image.open(self.filename)

        self.pic = bacon(self.image, self.s1.get(), self.s2.get(), self.s3.get(), self.s4.get(), self.s5.get())

        self.label.config(image=self.pic)
        
    def handle_slide(self):
        blur = self.s1.get()
        contrast = self.s2.get()
        brightness = self.s3.get()
        lower_sigma = self.s4.get()
        upper_sigma = self.s5.get()

        self.processed_img = bacon(self.image, blur, contrast, brightness, lower_sigma, upper_sigma)

        self.label.config(image=self.processed_img)

if __name__ == '__main__': 
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()