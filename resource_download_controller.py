import requests


# "requests" cannot download the resource, which includes YT (so, the system is only available for pictures)
def download(url, file_name):
    pic_dwl = requests.get(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
    )
    with open(file_name, "wb") as f:
        f.write(pic_dwl.content)


def image():
    image_dict = {
        "1": ("tiger", "https://upload.wikimedia.org/wikipedia/commons/3/3f/Walking_tiger_female.jpg"),
        "2": ("pig", "https://upload.wikimedia.org/wikipedia/commons/3/3e/Pig_farm_Vampula_1.jpg"),
        "3": ("wombat", "https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg")
    }
    print("welcome to image field")
    print("please select an image")
    while True:
        u_selec = input("please select an image: 1.tiger 2.piggy 3.wombat q.return to menu  ")
        if u_selec.upper() == "Q":
            return
        if u_selec not in image_dict.keys():
            print("please select an image again")
        else:
            print("you select number {}, {} ".format(u_selec, image_dict[u_selec][0]), image_dict[u_selec][1])
            url = image_dict[u_selec][1]
            file_name = "{}.jpg".format(image_dict[u_selec][0])
            download(url, file_name)


def journal():
    journal_dict = {
        "1": {
            "title": "The science of protests: how to shape public opinion and swing votes",
            "url": "https://www.nature.com/articles/d41586-024-02082-5"
        },
        "2": {
            "title": "How blockbuster obesity drugs create a full feeling — even before one bite of food",
            "url": "https://www.nature.com/articles/d41586-024-02106-0"
        },
        "3": {
            "title": "Bridge RNAs direct programmable recombination of target and donor DNA",
            "url": "https://www.nature.com/articles/s41586-024-07552-4"
        }
    }
    print("welcome to journal field")
    print("please select a journal")
    while True:
        u_selec = input("please select a journal: 1.science 2.drug 3.RNA q.return to menu  ")
        if u_selec.upper() == "Q":
            return
        if u_selec not in journal_dict.keys():
            print("please select a journal again")
        else:
            print("you select number {}. ".format(u_selec),
                  journal_dict[u_selec]["title"] + ", " + journal_dict[u_selec]["url"])


def video():
    video_dict = {
        "1": {
            "title": "Travel Tips for 4th of July Weekend",
            "url": "https://www.youtube.com/watch?v=o0Bz0XnXkfQ"
        },
        "2": {
            "title": "House Falls Into River After Rapidan Dam Collapses",
            "url": "https://www.youtube.com/watch?v=Ocg1Ui4R5BY"
        },
        "3": {
            "title": "Man Dies of Lightning Strike Trying to Warn Kids of Impending Storm",
            "url": "https://www.youtube.com/watch?v=fKAikkMCinM"
        }
    }
    print("welcome to video field")
    print("please select a video")
    while True:
        u_selec = input("please select a video: 1.travel 2.house 3.storm q.return to menu  ")
        if u_selec.upper() == "Q":
            return
        if u_selec not in video_dict.keys():
            print("please select a journal again")
        else:
            print("you select number {}. ".format(u_selec),
                  video_dict[u_selec]["title"] + ", " + video_dict[u_selec]["url"])


def run():
    func_list = {
        "1": image,
        "2": journal,
        "3": video
    }

    while True:
        choice_list = ["1", "2", "3"]
        user_choice = input("please select one of the following options: 1.pictupic_dwl 2.journals 3.videos q.exit ")
        if user_choice.upper() == "Q":
            break
        if user_choice not in choice_list:
            print("you need to select from 1 to 3")
        else:
            func_list[user_choice]()


run()
