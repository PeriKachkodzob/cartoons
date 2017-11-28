from bs4 import BeautifulSoup
import requests
from time import sleep

prevList = []
url = 'https://api.telegram.org/bot'
token = '466846728:AAGkdjZOYp1-zWIgFAmpLFPfM0o7xfVxIpk'
chat_id = 385220023

r = requests.get('https://toloka.to/f139')
soup = BeautifulSoup(r.text, 'lxml')
titleTags = soup.findAll('a', {'class':'topictitle'})

for tag in titleTags:
    title = tag.get_text()
    prevList.append(title)

def sendMessage(title):
    params = {'chat_id': chat_id, 'text': title}
    response = requests.post(url + token + '/sendMessage', data=params)
    return response

def main():
    global prevList
    while True:
        lastList = []
        r = requests.get('https://toloka.to/f139')
        soup = BeautifulSoup(r.text, 'lxml')
        titleTags = soup.findAll('a', {'class':'topictitle'})
        for tag in titleTags:
            title = tag.get_text()
            lastList.append(title)
            if title not in prevList:
                sendMessage(title)
        prevList = lastList
        sleep(3600)

main()
