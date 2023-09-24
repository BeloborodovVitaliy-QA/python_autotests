import requests

token = "f4e213dd4267da7d83ed915343498b86"
host = "https://api.pokemonbattle.me:9104"

response = requests.post("https://api.pokemonbattle.me:9104/pokemons", json={
    "name": "Бульб",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers={"Content-Type":"application/json","trainer_token":"f4e213dd4267da7d83ed915343498b86"})

print(response.text)


name = requests.put("https://api.pokemonbattle.me:9104/pokemons",json={
    "pokemon_id": "11168",
    "name": "жигари",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers={"Content-Type":"application/json", "trainer_token":"f4e213dd4267da7d83ed915343498b86"})

print(name.text)


in_pokeball = requests.post("https://api.pokemonbattle.me:9104/trainers/add_pokeball", json={
    "pokemon_id": "11168"
}, headers={"Content-Type":"application/json", "trainer_token":"f4e213dd4267da7d83ed915343498b86"})

print(in_pokeball.text)