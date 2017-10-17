import urllib
import re
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from time import strftime, localtime

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
#Purpose: Get the url page contents which the outgoing call reads from.
def cont():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    #https://www.twilio.com/docs/api/twiml/say
    resp.say("Hello Teikametrics. The top story on Hacker News for " + strftime("%A %B %-d %-I %M %p", localtime()) + " is: " + str(top_news()), voice="Alice", language="en-IN")
    return str(resp)

#Purpose: To fetch the top headline
def top_news():
    link="https://news.ycombinator.com/"
    f = urllib.urlopen(link)
    myfile = f.read()
    content =  myfile[0:5000]
    return re.search('class="storylink">(.*?)</a>', content).group(1)

if __name__ == "__main__":
    app.run(debug=True)

# Can DO:
# 1. Get an EST Time function
# 2. Find a better voice than Alice

# THOUGHTS:
# 1. Instead of ngrok, could use python libraries like BeautifulSoup, xlml.html, pandas
# 2. Used Cron for Scheduling
# 3. Can make time standard - 4 hours instead of using local time for consistency across locations  
