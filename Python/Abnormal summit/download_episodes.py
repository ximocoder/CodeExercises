from lxml import html
import requests

print("Begginning the download...")

page = requests.get('http://kshow123.net/show/abnormal-summit/')
try:
    tree = html.fromstring(page.content)
except:
    print("error")

#<div id="list-episodes">
#//*[@id="list-episodes"]/table/tbody/tr[1]

episodes = tree.xpath('//*[@id="list-episodes"]/table/tbody')

print("download done!")