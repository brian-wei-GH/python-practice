# python-practice
Some little examples in Python


## 🌕 resource_download_controller.py
this controller can download pictures from the internet when the users select the pictures they want. Also, the user can get the link to their favorite journals or videos

environment: {
    Python: 3.12.4,
    pycharm: 2024.1.3 pro,
    requests: 2.32.3
}

5 def : [ download(), image(), journal(), video(), run() ]


## 🌕 ticket_order_system.py
there are 4 functions in this system. 1. history (helping users to check their history orders) 2. booking (helping users to order the tickets) 3. delete file (giving users to delete their record) 4. run (main def)

for the booking system, there are 3 types of trains that the user can choose, and the maximum booking number is 200 tickets. 

the new users will create a file under the file "userbase"

the "CONTROL_V" is to avoid the error. When the users delete their files, the code cannot return to the "while CONTROL_V" loop. 

the "USER_FILE" needs to be stored in global is because all functions would use it. 

environment {
    Python: 3.12.4,
    pycharm: 2024.1.3 pro,
}


