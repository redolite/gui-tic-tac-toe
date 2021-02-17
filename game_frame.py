from tkinter import Frame, Label


class GameFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bg="blue")
        # Чтобы фрейм мог расширяться, необходимо настроить сетку на его
        # контейнере
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        label = Label(self, text="Label")
        label2 = Label(self, text="Label2", bg="red")
        # Параметр sticky дает возможность виджету занимать доступное место в
        # ячейке, расщиряясь за свои границы
        label.grid(column=1, row=1, sticky="nsew")
        label2.grid(column=0, row=0, sticky="nsew")

    def show(self):
        # Каждой колонке внутри сетки необходимо выдать weight
        # Это определяет, насколько широка ячейка
        # Например, столбец с weight=2 в два раза шире столбца с weight=1
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.grid(sticky="nsew")
