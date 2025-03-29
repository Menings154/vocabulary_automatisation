import json
import requests

ANKI_CONNECT_URL = "http://127.0.0.1:8765"

def add_card(deck_name, front, back):
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "Einfach",
                "fields": {
                    "Vorderseite": front,
                    "Rückseite": back
                },
                "tags": ["automated"],
                "options": {
                    "allowDuplicate": False
                }
            }
        }
    }
    
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()

def create_flash_cards(deck_name, voc_translated):
    for key in voc_translated.keys():
        add_card(deck_name=deck_name, front=key, back=voc_translated[key])
