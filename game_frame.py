from tkinter import Frame, Label, Button


class GameFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        # Чтобы фрейм мог расширяться, необходимо настроить сетку на его
        # контейнере
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        top_bar = Frame(self, height=50, width=100)
        top_bar.columnconfigure(0, weight=1)
        top_bar.columnconfigure(1, weight=1)
        top_bar.columnconfigure(2, weight=1)
        board = Frame(self)
        board.rowconfigure(0, weight=1)
        board.rowconfigure(1, weight=1)
        board.rowconfigure(2, weight=1)
        board.columnconfigure(0, weight=1)
        board.columnconfigure(1, weight=2)
        board.columnconfigure(2, weight=2)
        board.columnconfigure(3, weight=2)
        board.columnconfigure(4, weight=1)
        button00 = Button(board, text="T")
        button01 = Button(board, text="B")
        button02 = Button(board, text="X")
        button03 = Button(board, text="L")
        button04 = Button(board, text="P")
        button05 = Button(board, text="G")
        button06 = Button(board, text="V")
        button07 = Button(board, text="A")
        button08 = Button(board, text="Q")
        turn_counter = Label(top_bar, text='1 Ход')
        timer = Timer(top_bar)

        # Параметр sticky дает возможность виджету занимать доступное место в
        # ячейке, расщиряясь за свои границы
        top_bar.grid(row=0, column=0, columnspan=5, sticky="nsew")
        board.grid(row=1, column=0, columnspan=5, rowspan=3, sticky="nsew")
        button00.grid(row=0, column=1, sticky="nsew")
        button01.grid(row=1, column=3, sticky="nsew")
        button02.grid(row=1, column=2, sticky="nsew")
        button03.grid(row=1, column=1, sticky="nsew")
        button04.grid(row=0, column=2, sticky="nsew")
        button05.grid(row=0, column=3, sticky="nsew")
        button06.grid(row=2, column=3, sticky="nsew")
        button07.grid(row=2, column=1, sticky="nsew")
        button08.grid(row=2, column=2, sticky="nsew")
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
