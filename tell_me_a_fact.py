"""
Mashup to get a random fact from unkno.com, and then say it to you
"""

import os
import playsound
import requests
from gtts import gTTS
from bs4 import BeautifulSoup


def get_fact():
    """Gets a fact from unkno.com"""

    fact_page = requests.get("http://unkno.com/")
    scraped_data = BeautifulSoup(fact_page.text, 'html.parser')

    return scraped_data.find("div", {"id": "content"}).text


def say_fact(fact_text):
    """Says the fact (text to speech)"""

    tts = gTTS(fact_text)
    tts.save("temp.mp3")

    playsound.playsound('temp.mp3', True)

    os.remove("temp.mp3")


if __name__ == '__main__':
    say_fact(get_fact())
