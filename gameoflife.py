import tkinter as tk
from time import sleep
import random 

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.counter = 0

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
                
                self.button_arr[i].append(tk.Button(self, bg='white', height=1, width=2,
                                          command=on_click))

                self.button_arr[i][j].grid(row=i, column=j, sticky=tk.S)

        self.title = tk.Label(self, text="Game of Life", font=("Courier", 36))
        self.title.grid(row=0, column=25, columnspan=8)

        self.gen_number_text = tk.Label(self, text="Generation number:", font=("Courier", 12))
        self.gen_number_text.grid(row=1, column=28, columnspan=1)

        self.gen_number = tk.Label(self, text="0", font=("Courier", 12))
        self.gen_number.grid(row=1, column=29)

        self.rules1 = tk.Label(self, text="A black cell is alive. A white cell is dead. A cell's neighbors are adjacent")
        self.rules1.grid(row=2, column=25, columnspan=8)
        self.rules1 = tk.Label(self, text="vertically, horizontally, or diagonally. Evolution occurs according to these rules:")
        self.rules1.grid(row=3, column=25, columnspan=8)
        self.rules2 = tk.Label(self, text="1. Any live cell with two or three live neighbours survives.")
        self.rules2.grid(row=4, column=25, columnspan=8)
        self.rules3 = tk.Label(self, text="2. Any dead cell with three live neighbours becomes a live cell.")
        self.rules3.grid(row=5, column=25, columnspan=8)
        self.rules4 = tk.Label(self, text="3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.")
        self.rules4.grid(row=6, column=25, columnspan=8)

        self.play = tk.Button(self, text='Play', bg='white', command=self.on_play)
        self.play.grid(row=8, column=29)

        self.step = tk.Button(self, text='Step', bg='white', command=self.on_step)
        self.step.grid(row=8, column=30)

        self.clear = tk.Button(self, text='Clear', bg='white', command=self.clear_screen)
        self.clear.grid(row=8, column=31)

        self.stop = tk.Button(self, text='Stop', bg='white', command=self.on_stop)
        self.stop.grid(row=8, column=32, padx=(0, 10))

        self.blinker = tk.Button(self, text='Blinker', bg='white', command=self.on_blinker)
        self.blinker.grid(row=8, column=25, padx=(10, 0))

        self.glider = tk.Button(self, text='Glider', bg='white', command=self.on_glider)
        self.glider.grid(row=8, column=26)

        self.toad = tk.Button(self, text='Toad', bg='white', command=self.on_toad)
        self.toad.grid(row=8, column=27)

        self.random = tk.Button(self, text='Random', bg='white', command=self.on_random)
        self.random.grid(row=8, column=28, sticky=tk.W)

        self.message = tk.Message(self, text="The Game of Life is a cellular automaton created by British mathematician John Horton Conway. The game became widely known after being mentioned in a 1970 Scientific American article. The game consists of a collection of cells which live, die, or multiply based on mathematical principles.", font=("Courier", 12))
        self.message.config(aspect=200)
        self.message.grid(row=10, column=25, padx=(10, 0), columnspan=8, rowspan=14, sticky=tk.N)


    def get_neighbors(self, row, col):
        coords = [(row-1, col-1), (row-1, col), (row-1, col+1),
                  (row  , col-1),               (row  , col+1),
                  (row+1, col-1), (row+1, col), (row+1, col+1)]
        neighbors = []
        for r, c in coords:
            if (r > -1 and r < 25) and (c > -1 and c < 25):
                neighbors.append(self.button_arr[r][c])

        return neighbors
    
    def on_stop(self):
        self.keep_going = False
        self.blinker.config(state="normal")
        self.glider.config(state="normal")
        self.random.config(state="normal")
        self.step.config(state="normal")
        self.clear.config(state="normal")
        self.play.config(state="normal")
    
    def clear_screen(self):
        self.on_stop()

        for k in range(25):
            for f in range(25):
                self.button_arr[k][f].configure(bg='white')
        self.counter = 0
        self.gen_number['text'] = str(self.counter)

    def on_blinker(self):
        self.button_arr[10][9].configure(bg="black")
        self.button_arr[10][10].configure(bg="black")
        self.button_arr[10][11].configure(bg="black")

    def on_glider(self):
        self.button_arr[8][10].configure(bg="black")
        self.button_arr[9][11].configure(bg="black")
        self.button_arr[10][9].configure(bg="black")
        self.button_arr[10][10].configure(bg="black")
        self.button_arr[10][11].configure(bg="black")

    def on_toad(self):
        self.button_arr[10][9].configure(bg="black")
        self.button_arr[10][10].configure(bg="black")
        self.button_arr[10][11].configure(bg="black")
        self.button_arr[11][8].configure(bg="black")
        self.button_arr[11][9].configure(bg="black")
        self.button_arr[11][10].configure(bg="black")

    def on_random(self):
        for k in range(25):
            for f in range(25):
                random_color = random.choice(['black', 'white'])
                self.button_arr[k][f].configure(bg=random_color)

    def on_play(self):
        for k in range(25):
            for f in range(25):
                self.button_arr[k][f].config(state="disabled")
        self.blinker.config(state="disabled")
        self.glider.config(state="disabled")
        self.random.config(state="disabled")
        self.step.config(state="disabled")
        self.clear.config(state="disabled")
        self.play.config(state="disabled")

        self.keep_going = True
        while self.keep_going:
            self.apply_rules()
            sleep(0.2)
                        
        for k in range(25):
            for f in range(25):
                self.button_arr[k][f].config(state="normal")

    def on_step(self):
        self.apply_rules()

    def apply_rules(self):
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
                self.button_arr[r][c].update()

        # change generation number
        self.counter += 1
        self.gen_number['text'] = str(self.counter)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
