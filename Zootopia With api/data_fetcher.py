import requests

# ✅ Deine API-Infos (hier bitte deinen Key einsetzen!)
API_KEY = ''
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': { ... },
      'locations': [ ... ],
      'characteristics': { ... }
    }
    """
    url = API_URL.format(animal_name)
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # list of animal dicts
    else:
        print(f"⚠️ Error fetching data: {response.status_code}")
        return []
