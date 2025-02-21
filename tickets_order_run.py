import os
import shutil
import datetime


USER_FILE = "name"
CONTROL_V = True


def history():
    print("history")
    filename = os.path.join(USER_FILE, ' booking.txt')
    if not os.path.exists(filename):
        print("no history")
        shutil.rmtree(USER_FILE)
        return
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)


def booking():
    train_name = {
        "1": "train A",
        "2": "train B",
        "3": "train C",
    }
    ticket_num = [item for item in range(1, 201)]
    while True:
        select_train = input("please select a train, 1:train A, 2:train B, 3:train C: ")
        if select_train.upper() == "Q":
            return
        if select_train not in train_name.keys():
            print("please select a valid train")
        else:
            break
    while True:
        select_num = input("please select the number of the ticket from 1 to 200: ")
        if int(select_num) not in ticket_num:
            print("please enter a valid number")
        else:
            break
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    initial_data = "train name, ticket number, date\n"
    user_data = "{}, {}, {}.\n".format(train_name.get(select_train), select_num, date)
    filename = os.path.join(USER_FILE, ' booking.txt')
    with open(filename, 'a') as file:
        file.write(initial_data)
        file.write(user_data)


def delete_file():
    shutil.rmtree(USER_FILE)
    global CONTROL_V
    CONTROL_V = False
    return


def run():
    user = input('Enter your username: ')
    user_file = os.path.join("userbase", user)
    if user.upper() == "Q":
        return
    if not os.path.exists(user_file):
        os.makedirs(user_file)
        print("new user")
    else:
        print("welcome back")
    global USER_FILE
    USER_FILE = user_file

    func_dict = {
        "1": history,
        "2": booking,
        "3": delete_file,
    }

    while CONTROL_V:
        print("1. history, 2. booking, 3. delete file")
        user_choice = input("Enter your choice: ")
        if user_choice.upper() == "Q":
            return
        if user_choice not in func_dict.keys():
            print("invalid choice")
        else:
            func_dict[user_choice]()


if __name__ == '__main__':
    run()
