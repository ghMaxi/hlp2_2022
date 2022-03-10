from application import Application
from _thread import start_new_thread

from server import server_thread


def main():
    app = Application()
    start_new_thread(server_thread, (app.console_write,))
    app.mainloop()


if __name__ == "__main__":
    main()
