url="https://www.escape-metalcorner.at/de/events"

#from urllib.request import urlopen

#page = urlopen(url)

#html_bytes = page.read()
#html = html_bytes.decode("utf-8")

#print(html_bytes)


from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen(url)
#html = page.read().decode("utf-8")
html = page.read()
soup = BeautifulSoup(html, "html.parser")
#print(soup.get_text())
#print(soup.prettify())

events = soup.find_all("div", {"class": "eventday"})
print(type(events))
for event in events:
    #print(dir(event))
    #print(event.prettify())
    #print()
    datum = event.h2.text
    print("Datum:",  datum)
    #print("Url:", event.div.div.a['href'])
    title = event.div.div.a.div.img['title']
    print("Title:", title)
    #print("picture thumb:", event.div.div.a.div.img['src'])
    image_url = event.div.div.a.div.img['src'].replace('thumb.jpg','fullsize.jpg')
    print("image full:", image_url) 
    event_type = event.find('div').find_next('div').find_next('div').find_next('div').p.text 
    print("Event type:", event_type)
    
    #filename = image_url.split("/")[-1]
    #print(filename)
    #r = requests.get(title.strip(), stream = True)

    print("--")