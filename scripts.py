def get_photo(src, name='png.png'):
    import requests as rq
    r = rq.get(src)
    with open(name, 'wb') as photo:
        photo.write(r.content)


def get_weather(city='warszawa'):
    import requests as rq
    from bs4 import BeautifulSoup
    from PIL import Image
    import os

    r = rq.get(f'http://{city.lower()}.infometeo.pl/')
    soup = BeautifulSoup(r.content, 'html.parser')

    tag = soup.find('img', id="icm60h-meteogram")
    src = tag['src']

    ph_name = 'weather.png'
    with open(ph_name, 'wb') as new:
        photo = rq.get(src).content
        new.write(photo)

    with open(ph_name, 'rb') as photo:
        img = Image.open(photo)
        img.show()

    os.remove(ph_name)

