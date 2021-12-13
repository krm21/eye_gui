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
            font=Font(size=12), state=tk.DISABLED)
        self.s1.grid(row=1, column=1, pady=5)
        self.s1.bind('<Return>', lambda x: self.handle_slide())
        
        self.contrast_var = tk.IntVar(root)
        self.contrast_var.set(1)
        self.l2 = tk.Label(r, text="contrast")
        self.l2.grid(row=2, column=0, sticky=tk.W)
        self.s2 = tk.Spinbox(r, from_=0, to=20, command=lambda: self.handle_slide(), width=3, textvariable=self.contrast_var,
            font=Font(size=12), state=tk.DISABLED)
        self.s2.grid(row=2, column=1, pady=5)
        self.s2.bind('<Return>', lambda x: self.handle_slide())

        
        self.brightness_var = tk.IntVar(root)
        self.brightness_var.set(1)
        self.l3 = tk.Label(r, text="brightness")
        self.l3.grid(row=3, column=0, sticky=tk.W)
        self.s3 = tk.Spinbox(r, from_=0, to=10, command=lambda: self.handle_slide(), width=3, textvariable=self.brightness_var,
            font=Font(size=12), state=tk.DISABLED)
        self.s3.grid(row=3, column=1, pady=5)
        self.s3.bind('<Return>', lambda x: self.handle_slide())

        
        self.sigma_lower_var = tk.IntVar(root)
        self.sigma_lower_var.set(1)
        self.l4 = tk.Label(r, text="sigma lower")
        self.l4.grid(row=4, column=0, sticky=tk.W)
        self.s4 = tk.Spinbox(r, from_=0, to=30, command=lambda: self.handle_slide(), width=3, textvariable=self.sigma_lower_var,
            font=Font(size=12), state=tk.DISABLED)
        self.s4.grid(row=4, column=1, pady=5)
        self.s4.bind('<Return>', lambda x: self.handle_slide())

        
        self.sigma_upper_var = tk.IntVar(root)
        self.sigma_upper_var.set(20)
        self.l5 = tk.Label(r, text="sigma upper")
        self.l5.grid(row=5, column=0, sticky=tk.W)
        self.s5 = tk.Spinbox(r, from_=0, to=30, command=lambda: self.handle_slide(), width=3, textvariable=self.sigma_upper_var,
            font=Font(size=12), state=tk.DISABLED)
        self.s5.grid(row=5, column=1, pady=5)
        self.s5.bind('<Return>', lambda x: self.handle_slide())

        self.edge_var = tk.IntVar(root)
        self.edge_var.set(0)
        self.l6 = tk.Label(r, text="edge enhancement")
        self.l6.grid(row=6, column=0, sticky=tk.W)
        self.s6 = tk.Spinbox(r, from_=0, to=30, command=lambda: self.handle_slide(), width=3, textvariable=self.edge_var,
            font=Font(size=12), state=tk.DISABLED)
        self.s6.grid(row=6, column=1, pady=5)
        self.s6.bind('<Return>', lambda x: self.handle_slide())

        self.inverse_var = tk.BooleanVar(root)
        self.l7 = tk.Label(r, text="inverse colors")
        self.l7.grid(row=7, column=0, sticky=tk.W)
        self.c1 = tk.Checkbutton(r, variable=self.inverse_var, state=tk.DISABLED, command=lambda: self.handle_slide())
        self.c1.grid(row=7, column=1)

        self.filter_var = tk.StringVar(root)
        self.f1 = ttk.OptionMenu(r, self.filter_var,
            "Frangi",
            "Frangi",
            "Sato",
            "Meijering",
            "Hessian",
            command=lambda x: self.handle_slide(),
        )
        self.f1.configure(state='disabled')
        self.f1.grid(row=8, column=0, columnspan=2)

    def select_file(self):
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.')

        if self.filename:
            self._enable_spinners()

        self.image = Image.open(self.filename)

        self.pic = bacon(self.image, self.blur_var.get(), self.contrast_var.get(), self.brightness_var.get(), self.sigma_lower_var.get(), self.sigma_upper_var.get(), self.edge_var.get(), self.inverse_var.get(), self.filter_var.get())

        self.label.config(image=self.pic)
        
    def handle_slide(self):
        blur = self.blur_var.get()
        contrast = self.contrast_var.get()
        brightness = self.brightness_var.get()
        lower_sigma = self.sigma_lower_var.get()
        upper_sigma = self.sigma_upper_var.get()
        edge = self.edge_var.get()
        inverse = self.inverse_var.get()
        filter = self.filter_var.get()

        self.processed_img = bacon(self.image, blur, contrast, brightness, lower_sigma, upper_sigma, edge, inverse, filter)

        self.label.config(image=self.processed_img)

    def _enable_spinners(self):
        self.s1.config(state=tk.NORMAL)
        self.s2.config(state=tk.NORMAL)
        self.s3.config(state=tk.NORMAL)
        self.s4.config(state=tk.NORMAL)
        self.s5.config(state=tk.NORMAL)
        self.s6.config(state=tk.NORMAL)
        self.c1.config(state=tk.NORMAL)
        self.f1.configure(state='normal')


if __name__ == '__main__': 
    root = tk.Tk()
    root.geometry("800x600")
    MainWindow(root)
    root.mainloop()