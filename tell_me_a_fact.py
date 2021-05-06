"""
Mashup to get a random fact from unkno.com, and then say it to you
"""

import os
import playsound
import requests
from gtts import gTTS
from bs4 import BeautifulSoup


fact_page = requests.get("http://unkno.com/")
scraped_data = BeautifulSoup(fact_page.text, 'html.parser')

fact = scraped_data.find("div", {"id": "content"})

tts = gTTS(fact.text)
tts.save("temp.mp3")

playsound.playsound('temp.mp3', True)

os.remove("temp.mp3")
