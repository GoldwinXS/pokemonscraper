import requests
import bs4,os

target_url = 'https://pokemondb.net/sprites/'
save_folder = 'pokemon/'

request = requests.get(target_url,'GET')

soup = bs4.BeautifulSoup(request.content,'html.parser')

infocard_class = 'infocard'

infocards = soup.find_all(class_=infocard_class)

pokemon_links = []

for card in infocards:
    pokemon_links.append(target_url+card.text.lstrip(' '))


img_classes = ['img-fixed img-sprite-v1',
               'img-fixed img-sprite-v2',
               'img-fixed img-sprite-v3',
               'img-fixed img-sprite-v4',
               'img-fixed img-sprite-v5',
               'img-fixed img-sprite-v6',
               'img-fixed img-sprite-v7',
               'img-fixed img-sprite-v8',
               'img-fixed img-sprite-v9',
               'img-fixed img-sprite-v10',
               'img-fixed img-sprite-v11',
               'img-fixed img-sprite-v12',]

img_count = len(os.listdir(save_folder))
for pokemon_link in pokemon_links:
    request = requests.get(pokemon_link,'GET')
    soup = bs4.BeautifulSoup(request.content,'html.parser')
    img_links = []

    print('Saving images for: ',pokemon_link.lstrip(target_url))

    # for cls in img_classes:
    # tags = soup.find_all(class_=cls)

        # for tag in tags:
    try:
        srcs = [tag['src'] for tag in soup.find_all('img')]

        for src in srcs:
            with open(save_folder+str(img_count)+'.png','wb') as handle:
                img_count+=1
                resp = requests.get(src)
                handle.write(resp.content)
    except IndexError:
        print('IndexError encountered... ignoring... ')


