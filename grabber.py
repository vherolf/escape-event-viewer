url="https://www.escape-metalcorner.at/de/events"

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

from os.path import expanduser
from pathlib import Path

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def createFlyer(title, event_type, datum, image_url=None):
    namebydate = datum.split(', ')[1].replace('.','-')
    image_name = Path(home, 'images', title.replace(' ','-') + '-' + namebydate + '.jpg' )
    print(image_name)
    urlretrieve( image_url, image_name )

    img = Image.open(image_name)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("MetalMania-Regular.ttf", 40)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0),title ,(255,255,255),font=font)
    img.save(image_name)

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

    createFlyer(title, event_type, datum, image_url)


    print("--")
