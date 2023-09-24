from typing import Literal
import requests
import pytest


host = "https://api.pokemonbattle.me:9104"
token ="Cof4e213dd4267da7d83ed915343498b86"

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 1500})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.put(f'{host}/trainers', json={
    "name": "beliy",
    "city": "Tokyo"
},headers={"Content-Type":"application/json","trainer_token":"f4e213dd4267da7d83ed915343498b86"})
    
    assert response.json()["message"] == "Информация о тренере обновлена"

@pytest.mark.parametrize('key, value', [("trainer_name","beliy"),
                                        ("city","Tokyo"),
                                        ("id","1500")])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers', params={"trainer_id":1500})
    assert response.json()[key] == value