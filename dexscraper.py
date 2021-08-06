from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def show_html(URL_input):
       html = Request(URL_input, headers={'User-Agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'})
       return(urlopen(html).read())

pokemondb = BeautifulSoup(show_html("https://pokemondb.net/pokedex/national"),'html.parser')
# print(pokemondb.prettify())
all_pokemon = pokemondb.find_all("div", "infocard-list infocard-list-pkmn-lg")
for generation in all_pokemon:
       pokemon_per_gen = generation.find_all("div", "infocard")
       for pokemon in pokemon_per_gen:
              print(pokemon.find("span", "infocard-lg-data text-muted").small.string + "|" + pokemon.find("a", "ent-name").string)