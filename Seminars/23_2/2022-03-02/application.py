import tkinter
from tkinter.filedialog import askopenfile
from _thread import start_new_thread
from client import client_function


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        width, height, margin = 800, 600, 10
        text_width, text_height = 8, 16
        self.geometry(f"{width}x{height}")

        # создание текстовой консоли
        y = height - 2 * margin - 2 * text_height
        console = tkinter.Text(
            width=(width - 2 * margin) // text_width,
            height=y // text_height)
        console.place(x=margin, y=margin)
        console.config(state=tkinter.DISABLED)
        self.console = console

        # создание кнопки выбора файла
        y += 2 * margin
        button = tkinter.Button(text="Выбрать файл",
                                command=self.send_file)
        button.place(x=margin, y=y)

        # создание адресного поля
        address = tkinter.Text(width=15, height=1)
        address.insert(tkinter.END, '127.0.0.1:5000')
        button.update()
        x = button.winfo_width() + 2 * margin
        address.place(x=x, y=y)
        self.address = address

    def send_file(self):
        file = askopenfile(mode='rb')
        if file:
            address, port = self.address.get(1.0, "end-1c").split(':')
            send_address = address, int(port)
            start_new_thread(client_function, (file, send_address, self.console_write))
        else:
            self.console_write('no file')

    def console_write(self, message):
        self.console.config(state=tkinter.NORMAL)
        self.console.insert(tkinter.END, f'{message}\n')
        self.console.config(state=tkinter.DISABLED)
