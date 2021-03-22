from tkinter import Frame, Label, Button


class GameFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        # Чтобы фрейм мог расширяться, необходимо настроить сетку на его
        # контейнере
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        top_bar = Frame(self, height=50, width=100)
        for i in range(3):
            top_bar.columnconfigure(i, weight=1)
        board = Frame(self)
        for i in range(3):
            board.rowconfigure(i, weight=1)
        board.columnconfigure(0, weight=1)
        board.columnconfigure(1, weight=2)
        board.columnconfigure(2, weight=2)
        board.columnconfigure(3, weight=2)
        board.columnconfigure(4, weight=1)
        buttons = []
        for i in range(3):
            buttons_list = []
            for j in range(3):
                button = Button(board, text=i)
                buttons_list.append(button)
            buttons.append(buttons_list)

        turn_counter = Label(top_bar, text='1 Ход')
        timer = Timer(top_bar)

        # Параметр sticky дает возможность виджету занимать доступное место в
        # ячейке, расщиряясь за свои границы
        top_bar.grid(row=0, column=0, columnspan=5, sticky="nsew")
        board.grid(row=1, column=0, columnspan=5, rowspan=3, sticky="nsew")
        for i in range(3):
            for j in range(3):
                buttons[i][j].grid(row=i, column=j+1, sticky='nsew')
        turn_counter.grid(row=0, column=2, sticky="we")
        timer.grid(row=0, column=1, sticky='we')

    def show(self):
        # Каждой колонке внутри сетки необходимо выдать weight
        # Это определяет, насколько широка ячейка
        # Например, столбец с weight=2 в два раза шире столбца с weight=1
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)

        self.grid(sticky="nsew")

class Timer(Label):
    seconds = 0
    minutes = 0
    def __init__(self, master):
        super().__init__(master)
        self.count()

    def count(self):
        text = f'{self.minutes}:{self.seconds}'
        self.configure(text=text)
        self.seconds = self.seconds + 1
        if self.seconds >= 60:
            self.minutes = self.minutes + 1 
            self.seconds = 0
        self.after(1000, self.count)
