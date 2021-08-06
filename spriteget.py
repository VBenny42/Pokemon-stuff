from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import pprint
import pickle

from requests.api import get

def show_html(URL_input):
    # html = Request(URL_input, headers={'User-Agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'})
    page = requests.get(URL_input)
    return page.text


######### is not used. meta og is better #########
# def getlink(pokemon: dict):
#     test = "https://bulbapedia.bulbagarden.net/wiki/File:{0}{1}.png".format(pokemon['number'], pokemon['name'])
#     spritepage = BeautifulSoup(show_html(test),'html.parser')
#     sprite = spritepage.find("div", "fullImageLink")
#     t = sprite.find('a', href=True)
#     print(t['href'])

def getdex():
    national_dex = []
    dex_txt = open("national-dex.txt", "r")
    for line in dex_txt:
        pokemon = {}
        n_and_name = line.split("|")
        pokemon['number'] = n_and_name[0][1:]
        # name = re.sub(r'[^a-zA-Z0-9\' .-]', '', n_and_name[-1])
        pokemon['name'] = n_and_name[-1].replace(" ", "_").replace("\n", "")
        national_dex.append(pokemon)
    dex_txt.close()
    return national_dex
# pprint.pprint(national_dex)


def getimage(pokemon: dict):
    url = "https://bulbapedia.bulbagarden.net/wiki/{}_(Pokémon)".format(pokemon['name'])
    # print(url)
    page = BeautifulSoup(show_html(url), 'html.parser')
    image = page.find("meta", property="og:image")
    pokemon['imageurl'] = image["content"]
    print(image["content"])

def dumpdex(national_dex: list):
    dex_w_url = open("dex_with_url.pkl", "wb")
    pickle.dump(national_dex, dex_w_url)
    dex_w_url.close()

def loaddex():
    dex_w_url = open("dex_with_url.pkl", "rb")
    national_dex = pickle.load(dex_w_url)
    dex_w_url.close()
    return national_dex



####### this code loads from pkl file ########
# national_dex = loaddex()
# dex_txt = open("national-dex.txt", "r")
# index = 0
# for line in dex_txt:
#     print(line[:-1] + "|" + national_dex[index]["imageurl"])
#     index += 1


####### this one finds links ########
national_dex = getdex()
for pokemon in national_dex:
    getimage(pokemon)