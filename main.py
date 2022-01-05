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
        self.frame = ttk.Frame(root)
        self.frame.config(padding=(10, 10, 10, 10))
        self.frame.pack(side=tk.RIGHT)

        self.b1 = tk.Button(self.frame, text="Open an image...", command=self.select_file)
        self.b1.grid(row=0, column=0, pady=5, columnspan=2)

        self.s1, self.blur_var = self.add_spinbox("blur", 1, 0, 20, 1)
        self.s2, self.contrast_var = self.add_spinbox("contrast", 2, 0, 20, 1)
        self.s3, self.brightness_var = self.add_spinbox("brightness", 3, 0, 10, 1)
        self.s4, self.sigma_lower_var = self.add_spinbox("sigma lower", 4, 0, 30, 1)
        self.s5, self.sigma_upper_var = self.add_spinbox("sigma upper", 5, 20, 30, 1)
        self.s6, self.edge_var = self.add_spinbox("edge enhancement", 6, 0, 20, 1)

        self.inverse_var = tk.BooleanVar(root)
        self.l7 = tk.Label(self.frame, text="inverse colors")
        self.l7.grid(row=7, column=0, sticky=tk.W)
        self.c1 = tk.Checkbutton(self.frame, variable=self.inverse_var, state=tk.DISABLED, command=lambda: self.handle_slide())
        self.c1.grid(row=7, column=1)

        self.threshold_var = tk.BooleanVar(root)
        self.l8 = tk.Label(self.frame, text="otsu threshold")
        self.l8.grid(row=8, column=0, sticky=tk.W)
        self.c2 = tk.Checkbutton(self.frame, variable=self.threshold_var, state=tk.DISABLED, command=lambda: self.handle_slide())
        self.c2.grid(row=8, column=1)

        self.filter_var = tk.StringVar(root)
        self.f1 = ttk.OptionMenu(self.frame, self.filter_var,
            "Frangi",
            "Frangi",
            "Sato",
            "Meijering",
            "Hessian",
            command=lambda x: self.handle_slide(),
        )
        self.f1.configure(state='disabled')
        self.f1.grid(row=9, column=0, columnspan=2)

    def select_file(self):
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.')

        if self.filename:
            self._enable_spinners()

        self.image = Image.open(self.filename)

        self.pic = bacon(self.image, self.blur_var.get(), self.contrast_var.get(), self.brightness_var.get(), self.sigma_lower_var.get(), self.sigma_upper_var.get(), self.edge_var.get(), self.inverse_var.get(), self.threshold_var.get(), self.filter_var.get())

        self.label.config(image=self.pic)
        
    def handle_slide(self):
        blur = self.blur_var.get()
        contrast = self.contrast_var.get()
        brightness = self.brightness_var.get()
        lower_sigma = self.sigma_lower_var.get()
        upper_sigma = self.sigma_upper_var.get()
        edge = self.edge_var.get()
        inverse = self.inverse_var.get()
        threshold = self.threshold_var.get()
        filter = self.filter_var.get()

        self.processed_img = bacon(self.image, blur, contrast, brightness, lower_sigma, upper_sigma, edge, inverse, threshold, filter)

        self.label.config(image=self.processed_img)

    def _enable_spinners(self):
        self.s1.config(state=tk.NORMAL)
        self.s2.config(state=tk.NORMAL)
        self.s3.config(state=tk.NORMAL)
        self.s4.config(state=tk.NORMAL)
        self.s5.config(state=tk.NORMAL)
        self.s6.config(state=tk.NORMAL)
        self.c1.config(state=tk.NORMAL)
        self.c2.config(state=tk.NORMAL)
        self.f1.configure(state='normal')

    def add_spinbox(self, text, row, lower, upper, default):
        state_var = tk.IntVar(root)
        state_var.set(default)
        l = tk.Label(self.frame, text=text)
        l.grid(row=row, column=0, sticky=tk.W)
        s = tk.Spinbox(self.frame, from_=lower, to=upper, command=lambda: self.handle_slide(), width=3, textvariable=state_var, font=Font(size=12), state=tk.DISABLED)
        s.grid(row=row, column=1, pady=5)
        s.bind('<Return>', lambda x: self.handle_slide())
        return s, state_var

if __name__ == '__main__': 
    root = tk.Tk()
    root.geometry("800x600")
    MainWindow(root)
    root.mainloop()