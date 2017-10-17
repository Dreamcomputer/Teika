from twilio.rest import Client
import json
import os

# Purpose: To make the url public
os.system('./ngrok http 5000 > /dev/null &')
os.system('curl  http://localhost:4040/api/tunnels > ip.json')
with open('ip.json') as content:
    jsoncont = json.load(content)
a = jsoncont['tunnels'][1]['public_url']

# To get credentials from http://twilio.com/user/account
account_sid = "ACf430019e836dacdfe7228351d1ba28ae"
auth_token = "5860a2d2a680c2e31b9e4d319d54ef7b"
client = Client(account_sid, auth_token)

# To make a call
call = client.api.account.calls\
       .create(to="+17035896894", #Teika number
               from_="+16177516645", # my twilio number
               url=a)

print(call.sid)

