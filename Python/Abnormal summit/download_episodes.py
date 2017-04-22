from lxml import html
import requests

print("Begginning the download...")

page = requests.get('http://drama3s.com/watch/abnormal-summit-episode-1-693_9556.html')

try:
    tree = html.fromstring(page.content)
except:
    print("error")

#<div id="list-episodes">
#//*[@id="list-episodes"]/table/tbody/tr[1]

episodes = tree.xpath('//*[@id="list-episodes"]/table/tbody')

print("download done!")