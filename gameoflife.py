import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button_arr = [[] for i in range(25)]

        for i in range(25):
            for j in range(25):
    
                def on_click(row=i, col=j):
                    cur_color = self.button_arr[row][col]['bg']

                    # based on the current color, set the opposite color
                    if cur_color == "black":
                        self.button_arr[row][col].configure(bg="white")
                    if cur_color == "white":
                        self.button_arr[row][col].configure(bg="black")
                
                self.button_arr[i].append(tk.Button(self, text='   ', bg='white',
                                          command=on_click))

                self.button_arr[i][j].grid(row=i, column=j)

        self.play = tk.Button(self, text='Play', bg='white', command=self.on_play)
        self.play.grid(row=4, column=27)

    def get_neighbors(self, row, col):
        n1 = self.button_arr[0][1]
        n2 = self.button_arr[1][1]
        n3 = self.button_arr[1][0]
        return [n1, n2, n3]

    def on_play(self):
        for k in range(25):
            for f in range(25):
                self.button_arr[k][f].config(state="disabled")

        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        bg_black_list = []
        for n in self.get_neighbors(0, 0):
            bg = n['bg']
            bg_black_list.append(bg == 'black')

        # bg_black_list = [bg1 == 'black', bg2 == 'black', bg3 == 'black']
        count_bg_black = bg_black_list.count(True)

        if self.button_arr[0][0]['bg'] == 'black':
            if count_bg_black >= 2 and count_bg_black <= 3:
                self.button_arr[0][0].configure(bg="black")
            else:
                self.button_arr[0][0].configure(bg="white")
        if self.button_arr[0][0]['bg'] == 'white':
            if count_bg_black == 3:
                self.button_arr[0][0].configure(bg="black")

        for k in range(25):
            for f in range(25):
                self.button_arr[k][f].config(state="normal")
        
        


root = tk.Tk()
app = Application(master=root)
app.mainloop()
