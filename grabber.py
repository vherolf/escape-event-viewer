url="https://www.escape-metalcorner.at/de/events"

from bs4 import BeautifulSoup
from urllib.request import urlopen

from os.path import expanduser
from pathlib import Path


home = Path.home()
playlist = Path(home, 'playlist')
# delete content of the file
open(playlist, 'w').close()
playlist.chmod(0o000600)

page = urlopen(url)
html = page.read()
soup = BeautifulSoup(html, "html.parser")

events = soup.find_all("div", {"class": "eventday"})
print(type(events))

for event in events:
    datum = event.h2.text
    print("Datum:",  datum)

    title = event.div.div.a.div.img['title']
    print("Title:", title)

    image_url = event.div.div.a.div.img['src'].replace('thumb.jpg','fullsize.jpg')
    print("image full:", image_url) 
    event_type = event.find('div').find_next('div').find_next('div').find_next('div').p.text 
    print("Event type:", event_type)

    print("--")
