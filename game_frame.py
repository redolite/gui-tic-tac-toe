from tkinter import Frame, Label, Button, StringVar, messagebox

NAMES_DICTIONARY = {
    'X': 'Крестики',
    'O': 'Нолики' 
}

class GameFrame(Frame):
    def __init__(self, master):
        self.table = {}
        self.active_player = 'X'
        self.current_turn = 1
        self.turn_string = StringVar(value=f'Ход {self.current_turn}')
        self.is_game_finished = False
        super().__init__(master)
        # Чтобы фрейм мог расширяться, необходимо настроить сетку на его
        # контейнере
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        top_bar = Frame(self, height=50, width=100)
        self.timer = Timer(top_bar)
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

        # Параметр sticky дает возможность виджету занимать доступное место в
        # ячейке, расщиряясь за свои границы
        top_bar.grid(row=0, column=0, columnspan=5, sticky="nsew")
        board.grid(row=1, column=0, columnspan=5, rowspan=3, sticky="nsew")
        for i in range(3):
            for j in range(3):
                buttons[i][j].grid(row=i, column=j+1, sticky='nsew')
        turn_counter.grid(row=0, column=2, sticky="we")
        self.timer.grid(row=0, column=1, sticky='we')

    def show(self):
        # Каждой колонке внутри сетки необходимо выдать weight
        # Это определяет, насколько широка ячейка
        # Например, столбец с weight=2 в два раза шире столбца с weight=1
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)

        self.grid(sticky="nsew")

    def handle_turn(self, cell_row, cell_column):
        if self.table[f'cell{cell_row}-{cell_column}'].get() == '' and not self.is_game_finished:
            print('Active Player:', self.active_player)
            self.table[f'cell{cell_row}-{cell_column}'].set(self.active_player)
            print(self.table)
            if self.current_turn >= 5:
                self.is_game_finished = self.check_for_victory(cell_row, cell_column)
                print(self.is_game_finished)
            if not self.is_game_finished:
                if self.current_turn < 9:
                    self.switch_active_player()
                    self.update_turn_count()
                else: 
                    self.end_game(stalemate=True)
            else:
                self.end_game()

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

    def check_for_victory(self, cell_row, cell_column):
        results_in_row = [self.table[f'cell{cell_row}-{i}'].get() for i in range(3)]
        results_in_column = [self.table[f'cell{i}-{cell_column}'].get() for i in range(3)]
        if all(r == self.active_player for r in results_in_row):
            return True
        if all(r == self.active_player for r in results_in_column):
            return True
        should_check_main_diagonal = cell_row == cell_column
        should_check_second_diagonal = (cell_row == 0 and cell_column == 2) or (cell_row == 1 and cell_column == 1) or (cell_row == 2 and cell_column == 0)
        if should_check_main_diagonal:
            results_in_main_diagonal = [self.table[f'cell{i}-{i}'].get() for i in range(3)]
            if all(r == self.active_player for r in results_in_main_diagonal):
                return True
        if should_check_second_diagonal:
            results_in_second_diagonal = [self.table[f'cell{i}-{2-i}'].get() for i in range(3)]
            if all(r == self.active_player for r in results_in_second_diagonal):
                return True
        return False 
    
    def end_game(self, stalemate = False):
        self.timer.stop()
        if stalemate:
            print('Stalemate!')
            messagebox.showinfo('Ничья!', 'Ничья!')
        else:
            print(f'''{self.active_player} !''')
            messagebox.showinfo('Победа!', f'{NAMES_DICTIONARY[self.active_player]} победили!')
        restart_game = messagebox.askyesno('Играть снова?', 'Вы хотите перезапустить игру?')
        if not restart_game:
            self.destroy()                   
        


class Timer(Label):
    seconds = 0
    minutes = 0
    is_running = True
    def __init__(self, master):
        super().__init__(master)
        self.__count()

    def __count(self):
        text = f'{self.minutes}:{self.seconds:02d}'
        self.configure(text=text)
        self.seconds = self.seconds + 1
        if self.seconds >= 60:
            self.minutes = self.minutes + 1 
            self.seconds = 0
        if self.is_running:
            self.after(1000, self.__count)
    
    def stop(self):
        self.is_running = False        