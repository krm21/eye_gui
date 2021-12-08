import tkinter as tk
from tkinter import PhotoImage, Variable, ttk
from tkinter import filedialog as fd
from tkinter.font import Font

import PIL
from PIL import Image
from filter import bacon

class MainWindow:
    def __init__(self, root):
        self.label = ttk.Label(root)
        self.label.pack(side=tk.LEFT)
        r = ttk.Frame(root)
        r.config(padding=(10, 10, 10, 10))
        r.pack(side=tk.RIGHT)

        self.b1 = tk.Button(r, text="Open an image...", command=self.select_file)
        self.b1.grid(row=0, column=0, pady=5, columnspan=2)

        self.blur_var = tk.IntVar(root)
        self.blur_var.set(1)
        self.l1 = tk.Label(r, text="blur")
        self.l1.grid(row=1, column=0, sticky=tk.W)
        self.s1 = tk.Spinbox(r, from_=0, to=20, command=lambda: self.handle_slide(), width=3, textvariable=self.blur_var,
            font=Font(size=12))
        self.s1.grid(row=1, column=1, pady=5)
        
        self.contrast_var = tk.IntVar(root)
        self.contrast_var.set(1)
        self.l2 = tk.Label(r, text="contrast")
        self.l2.grid(row=2, column=0, sticky=tk.W)
        self.s2 = tk.Spinbox(r, from_=0, to=20, command=lambda: self.handle_slide(), width=3, textvariable=self.contrast_var,
            font=Font(size=12))
        self.s2.grid(row=2, column=1, pady=5)
        
        self.brightness_var = tk.IntVar(root)
        self.brightness_var.set(1)
        self.l3 = tk.Label(r, text="brightness")
        self.l3.grid(row=3, column=0, sticky=tk.W)
        self.s3 = tk.Spinbox(r, from_=0, to=10, command=lambda: self.handle_slide(), width=3, textvariable=self.brightness_var,
            font=Font(size=12))
        self.s3.grid(row=3, column=1, pady=5)
        
        self.sigma_lower_var = tk.IntVar(root)
        self.sigma_lower_var.set(1)
        self.l4 = tk.Label(r, text="sigma lower")
        self.l4.grid(row=4, column=0, sticky=tk.W)
        self.s4 = tk.Spinbox(r, from_=0, to=30, command=lambda: self.handle_slide(), width=3, textvariable=self.sigma_lower_var,
            font=Font(size=12))
        self.s4.grid(row=4, column=1, pady=5)
        
        self.sigma_upper_var = tk.IntVar(root)
        self.sigma_upper_var.set(20)
        self.l5 = tk.Label(r, text="sigma upper")
        self.l5.grid(row=5, column=0, sticky=tk.W)
        self.s5 = tk.Spinbox(r, from_=0, to=30, command=lambda: self.handle_slide(), width=3, textvariable=self.sigma_upper_var,
            font=Font(size=12))
        self.s5.grid(row=5, column=1, pady=5)

    def select_file(self):
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.')

        self.image = Image.open(self.filename)

        self.pic = bacon(self.image, self.blur_var.get(), self.contrast_var.get(), self.brightness_var.get(), self.sigma_lower_var.get(), self.sigma_upper_var.get())

        self.label.config(image=self.pic)
        
    def handle_slide(self):
        blur = self.blur_var.get()
        contrast = self.contrast_var.get()
        brightness = self.brightness_var.get()
        lower_sigma = self.sigma_lower_var.get()
        upper_sigma = self.sigma_upper_var.get()

        self.processed_img = bacon(self.image, blur, contrast, brightness, lower_sigma, upper_sigma)

        self.label.config(image=self.processed_img)

if __name__ == '__main__': 
    root = tk.Tk()
    root.geometry("800x600")
    MainWindow(root)
    root.mainloop()