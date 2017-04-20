from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib.request
import sys, os, tempfile, logging
import urllib.request as urllib2
import urllib.parse as urlparse


def download_file(url, desc=None):
    u = urllib2.urlopen(url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = desc

    with open(filename, 'wb') as f:
        meta = u.info()
        meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])
        print("Downloading: {0} Bytes: {1}".format(url, file_size))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = "{0:16}".format(file_size_dl)
            if file_size:
                status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
            status += chr(13)
            print(status, end="")
        print()

    return filename



def printme(str):
   print(str)
   return

def checkURL(str):
    filename = "H:\\Abnormal sumit\\" + str.split('/')[5].replace('.html', '') + ".mp4"

    if os.path.isfile(filename):
        print("already exists! " + filename)
        return

    print("downloading " + filename)
    driver = webdriver.Chrome()
    driver.get(str)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    res = soup.find_all(class_="jw-video jw-reset")
    #sres = str(res)
    for link in res:
        sourcefile = link.get("src")

        printme(link.get("src"))
        #urllib.request.urlretrieve(sourcefile, filename)
        if not os.path.isfile(filename):
            download_file(sourcefile, filename)

    driver.stop_client()
    driver.quit
    driver.close
    return


print("Beginning the videos download...")

url = 'http://kshow123.net/show/abnormal-summit/'
url2 = 'http://drama3s.com/watch/abnormal-summit-episode-1-693_9556.html'

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

for link in soup.find_all('a'):
    #print(link.get('href'))
    if 'episode-' in str(link.get('href')):
        #printme(link.get('href'))
        checkURL(link.get('href'))


print("done! :)")
