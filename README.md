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


## 🌕 diary_recoder_with_mins.py
the function is to create diaries min by min

environment {
    Python: 3.12.4,
    pycharm: 2024.1.3 pro, 
}


## 🔆 analyzing_historical_stock_data/revenue_project
analyzing historical stock data revenue project with DS

the project has 6 questions 
1. using yfinance to extract Tesla historical stock data
2. using web-scraping to extract Tesla revenue data
3. using yfinance to extract GameStop historical stock data
4. using web-scraping to extract GameStop revenue data
5. plot Tesla stock graph
6. plot GameStop stock graph

environment: {
    python: 3.12.4,
    pycharm: 2024,1,3 pro
}

Tesla Quarterly Revenue web link: "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"  # for question 2 
GameStop Quarterly Revenue web link: "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue" # for question 4


## 🌕 extract_data_excel
extracting data from excel file

the first function is to extract data from the "countries" sheet and 'Government' segment. Also, the 'Units Sold' more than 1000 times.
1. output includes country, units sold, sales, profits, and date
2. count how many times Germany appears in Government segment

the second function is to find the highest quality among all professors

environment: {
    python:3.12.4,
    pycharm: 2024.1.3 pro
}
