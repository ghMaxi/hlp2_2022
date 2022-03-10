import tkinter
from tkinter.filedialog import askopenfile
from client import send_file
from constants import server_address


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        width, height, margin = 800, 600, 5
        symbol_width, symbol_height = 8, 16
        self.geometry(f'{width}x{height}')

        # текстовая консоль
        y = height - 2 * margin - 2 * symbol_height
        self.console = tkinter.Text(
            width=(width - 2 * margin) // symbol_width,
            height=y // symbol_height)
        self.console.place(x=margin, y=margin)
        self.print("Начало работы")

        # кнопка загрузки файлов
        button = tkinter.Button(text='Выбрать файл',
                                command=self.file_select)
        button.place(x=margin, y=y + margin * 2)

        # адрес сервера
        self.address = tkinter.Text(height=1)
        self.address.insert(
            tkinter.END,
            f"{server_address[0]}:{server_address[1]}")
        button.update()
        self.address.place(x=margin * 2 + button.winfo_width(),
                           y=y + margin * 2)

    def file_select(self):
        file = askopenfile(mode='rb')
        if file:
            send_file(file, self.print)
            file.close()
        else:
            self.print('no file')

    def print(self, message):
        self.console.config(state=tkinter.NORMAL)
        self.console.insert(tkinter.END, f"{message}\n")
        self.console.config(state=tkinter.DISABLED)
