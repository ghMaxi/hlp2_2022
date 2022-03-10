import tkinter
from tkinter import filedialog

import network


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        width, height, margin = 800, 600, 5
        text_height, text_width = 16, 8
        self.geometry(f"{width}x{height}")
        self.info_text = tkinter.Text(
            width=(width - 2 * margin) // text_width,
            height=(7 * height // 8) // text_height)
        self.info_text.place(x=margin, y=margin)
        self.info_text.insert(tkinter.END, "Program started")
        self.info_text.config(state=tkinter.DISABLED)

        # ip input
        ip_label = tkinter.Label(text="target IP:")
        y = height - margin * 4 - text_height
        ip_label.place(x=margin * 4, y=y)
        ip_label.update()
        x = ip_label.winfo_x() + ip_label.winfo_width() + text_width
        self.ip1, self.ip2, self.ip3, self.ip4 = (tkinter.Text(width=3, height=1) for _ in range(4))
        for ip in self.ip1, self.ip2, self.ip3, self.ip4:
            ip.place(x=x, y=y)
            x += text_width * 4
        x -= text_width
        for text_label in (tkinter.Label(text='.') for _ in range(3)):
            x -= text_width * 4
            text_label.place(x=x, y=y)

        # send file
        file_button = tkinter.Button(text='Send a File', command=self.select_file)
        file_button.place(x=margin * 4, y=y - text_height * 2)

    def select_file(self):
        filetypes = (('png images', '*.png'),
                     ('jpg images', '*.jpg'))
        file = filedialog.askopenfile(filetypes=filetypes)
        if file:
            network.start_send_file_thread(file, self.text_message)
        else:
            self.text_message('No file')

    def text_message(self, message):
        self.info_text.config(state=tkinter.NORMAL)
        self.info_text.insert(tkinter.END, f"\n{message}")
        self.info_text.config(state=tkinter.DISABLED)
