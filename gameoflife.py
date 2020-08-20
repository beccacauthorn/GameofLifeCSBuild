import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button_list = []
        for i in range(25):
            self.button_list.append(tk.Button(self, text='   ', bg='white'))
            self.button_list[-1].grid(row=1, column=i)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
