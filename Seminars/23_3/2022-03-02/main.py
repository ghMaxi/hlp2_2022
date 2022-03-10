from application import Application
from _thread import start_new_thread
from server import main as server_func


def main():
    app = Application()
    start_new_thread(
        server_func, (app.print,))
    app.mainloop()


if __name__ == "__main__":
    main()
