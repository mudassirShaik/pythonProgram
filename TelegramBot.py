import requests

api_URL = "https://api.telegram.org/bot1897607188:AAGKQahxETtNKJizNxfzSN-RmgCJ9SeoL5k/sendMessage?chat_id=-550067442&text="

def sendMsg(msg):
    send_msg = api_URL + msg
    response = requests.get(send_msg)
    return response.json()
    
sendMsg("Helloorld")