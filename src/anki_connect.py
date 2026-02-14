import requests
import json

with open("./src/config.json", "r") as file:
  config = json.load(file)

def add_note(front, back, deck=config.get("DECK_NAME")):
  '''
  It sends a post request to Ankiconnect to create a card
  '''

  payload = {
    "action": "addNote",
    "version": "6",
    "params": {
      "note": {
        "deckName": deck,
        "modelName": "Basic",
        "fields":{
          "Front": front,
          "Back": back
        },
        "tags": ["cli_added", "english"]
      }
    }
  }
  try:
    response = requests.post(config.get("ANKI_URL"), json=payload)
    result = response.json()

    if result.get("error"):
      return False, f"Anki intern error: {result["error"]}"
    return True, f"Card sent with id: {result["result"]}"
  except requests.exceptions.ConnectionError:
    return False, "Cannot connect with Anki. It's open?"