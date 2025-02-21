import datetime


def run():
    while True:
        text = input("Enter your text: ")
        if text.upper() == "Q":
            break
        date = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
        text = "{}\n".format(text)
        with open(date, "a") as f:
            f.write(text)


if __name__ == '__main__':
    run()
