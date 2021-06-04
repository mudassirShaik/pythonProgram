#Libraries Import
import requests
from datetime import datetime
import time

#Project Init
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
pinCode = 500018
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pinCode, today_date)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

#check Avalibility
def findAvailability():
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity"] >= 0) & (each["min_age_limit"] == 18)):
            message = "Name: {}, \nAddress: {}, \nType: {}, \nAvailability: {}, \nBrand: {}, \nAge: {}\n\n".format(
                each["name"], each["address"], each["fee_type"],
                each["available_capacity_dose1"], each["vaccine"],
                each["min_age_limit"])
            #sendMsg(message)
            print(message)

#Telegram Bot
api_URL = "https://api.telegram.org/bot1897607188:AAGKQahxETtNKJizNxfzSN-RmgCJ9SeoL5k/sendMessage?chat_id=-550067442&text="

def sendMsg(message):
    send_msg = api_URL + message
    response = requests.get(send_msg)
    return response.json()

#Sleep
while(findAvailability() != True):
    time.sleep(10)
    findAvailability()