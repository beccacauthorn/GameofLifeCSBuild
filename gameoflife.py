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
        coords = [(row-1, col-1), (row-1, col), (row-1, col+1),
                  (row  , col-1),               (row  , col+1),
                  (row+1, col-1), (row+1, col), (row+1, col+1)]
        neighbors = []
        for r, c in coords:
            if (r > -1 and r < 25) and (c > -1 and c < 25):
                neighbors.append(self.button_arr[r][c])

        return neighbors

    def on_play(self):
        for k in range(25):
            for f in range(25):
                self.button_arr[k][f].config(state="disabled")

        future_colors = []
        for x in range(25):
            future_colors.append([])
            for y in range(25):
                future_colors[-1].append("white")

        # apply the rules and build a separate grid of future values
        for r in range(25):
            for c in range(25):
                # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                bg_black_list = []
                for n in self.get_neighbors(r, c):
                    bg = n['bg']
                    bg_black_list.append(bg == 'black')

                # bg_black_list = [bg1 == 'black', bg2 == 'black', bg3 == 'black']
                count_bg_black = bg_black_list.count(True)

                if self.button_arr[r][c]['bg'] == 'black':
                    if count_bg_black >= 2 and count_bg_black <= 3:
                        future_colors[r][c] = "black"
                    else:
                        future_colors[r][c] = "white"
                if self.button_arr[r][c]['bg'] == 'white':
                    if count_bg_black == 3:
                        future_colors[r][c] = "black"

        # using the newly built grid of values, change all colors at the same time
        for r in range(25):
            for c in range(25):
                self.button_arr[r][c].configure(bg=future_colors[r][c])
                self.button_arr[r][c].config(state="normal")



root = tk.Tk()
app = Application(master=root)
app.mainloop()
