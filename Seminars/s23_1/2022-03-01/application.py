import tkinter
from tkinter import filedialog
from _thread import start_new_thread

from client import client_thread
from constants import server_address


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.height, width, self.margin = 600, 800, 5
        self.text_height, self.text_width = 16, 8

        self.geometry(f"{width}x{self.height}")

        # консоль сообщений
        self.console = tkinter.Text(
            width=(width - 2 * self.margin) // self.text_width,
            height=(self.height * 0.76 - 2 * self.margin) // self.text_height)
        self.console.place(x=self.margin, y=self.margin)
        self.console_write("Начало работы")

        self.ips = self.make_ip_input()

        button = tkinter.Button(text="Send file", command=self.select_file)
        button.place(x=self.margin * 4,
                     y=self.height - 4 * self.margin - 3 * self.text_height)

    def console_write(self, message):
        self.console.config(state=tkinter.NORMAL)
        self.console.insert(tkinter.END, f"{message}\n")
        self.console.config(state=tkinter.DISABLED)

    def select_file(self):
        file = filedialog.askopenfile(mode='rb')  # from tkinter import filedialog
        if file:
            address = ('.'.join(ip.get("1.0", tkinter.END).strip()
                                for ip in self.ips)
                       + f':{server_address[1]}')
            start_new_thread(client_thread,
                             (file, address, self.console_write))
        else:
            self.console_write('no file')

    def make_ip_input(self):
        ips = tuple(tkinter.Text(width=3, height=1) for _ in range(4))
        labels = tuple(tkinter.Label(text='.') for _ in range(4))
        numbers = server_address[0].split('.')

        text = "Server IP:"
        labels[0].config(text=text)
        y = self.height - self.margin * 4 - self.text_height
        x = self.margin * 4
        labels[0].place(x=x, y=y)
        labels[0].update()
        x += labels[0].winfo_width() + self.text_width
        ips[0].place(x=x, y=y)
        ips[0].insert(tkinter.END, numbers[0])
        for i in range(1, 4):
            x += self.text_width * 3
            labels[i].place(x=x, y=y)
            x += self.text_width
            ips[i].place(x=x, y=y)
            ips[i].insert(tkinter.END, numbers[i])

        return ips
