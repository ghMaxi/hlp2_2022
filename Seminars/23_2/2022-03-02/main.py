from application import Application
from server import main as server_start
from _thread import start_new_thread


def main():
    app = Application()
    start_new_thread(
        server_start, (app.console_write,))
    app.mainloop()


if __name__ == "__main__":
    main()
