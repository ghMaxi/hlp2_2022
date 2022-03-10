import network


def main():
    filename = input(
        "Введите имя посылаемого файла (по умолчанию test.png): ")
    if filename == '':
        filename = 'test.png'
    lock = network.send(filename)
    while lock.locked():
        pass
    print("done")


if __name__ == "__main__":
    main()
