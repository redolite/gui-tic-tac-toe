from tkinter import Frame, Label, Button, StringVar


class GameFrame(Frame):
    def __init__(self, master):
        self.table = {}
        self.active_player = 'X'
        self.current_turn = 1
        self.turn_string = StringVar(value=f'Ход {self.current_turn}')
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
                self.table[f'cell{i}-{j}'] = StringVar(value='')
                button = Button(board, textvariable = self.table[f'cell{i}-{j}'], command=lambda arg1=i, arg2=j: self.handle_turn(arg1, arg2))
                buttons_list.append(button)
            buttons.append(buttons_list)
        turn_counter = Label(top_bar, textvariable=self.turn_string) # текст в лейбле можно соеденить со значением переменной(прочитать)
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

    def handle_turn(self, cell_row, cell_column):
        if self.table[f'cell{cell_row}-{cell_column}'].get() == '':
            print('Active Player:', self.active_player)
            self.table[f'cell{cell_row}-{cell_column}'].set(self.active_player)
            print(self.table)
            self.switch_active_player()
            self.update_turn_count()

    def switch_active_player(self):
        if self.active_player == 'X':
            self.active_player = 'O'
        elif self.active_player == 'O':
            self.active_player = 'X'

    def update_turn_count(self):
        self.current_turn = self.current_turn + 1
        self.turn_string.set(f'Ход {self.current_turn}')
        print("current_turn:", self.current_turn)
        print("turn_string:", self.turn_string.get())



class Timer(Label):
    seconds = 0
    minutes = 0
    def __init__(self, master):
        super().__init__(master)
        self.count()

    def count(self):
        text = f'{self.minutes}:{self.seconds:02d}'
        self.configure(text=text)
        self.seconds = self.seconds + 1
        if self.seconds >= 60:
            self.minutes = self.minutes + 1 
            self.seconds = 0
        self.after(1000, self.count)
