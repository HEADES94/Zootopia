import requests

API_KEY = '6RjGMiEH2vg6v8K4t7RCjw==orUDtroNLA1eLSAs'
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'

def fetch_animals_from_api(query):
    """Fetches animal data from the API Ninja Animals API."""
    url = API_URL.format(query)
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()  # returns a list

def generate_animal_card(animal):
    """Generates HTML for a single animal card."""
    parts = []
    name = animal.get('name')
    taxonomy = animal.get('taxonomy', {})
    characteristics = animal.get('characteristics', {})
    locations = animal.get('locations')

    if name:
        parts.append(f"<h2>{name}</h2>")
    if 'scientific_name' in taxonomy:
        parts.append(f"<p><strong>Scientific Name:</strong> {taxonomy['scientific_name']}</p>")
    if locations:
        parts.append(f"<p><strong>Location:</strong> {', '.join(locations)}</p>")
    if 'diet' in characteristics:
        parts.append(f"<p><strong>Diet:</strong> {characteristics['diet']}</p>")

    return f'<li class="cards__item">\n' + "\n".join(parts) + '\n</li>'

def main():
    template_path = '../Zootopia/animals_template.html'
    output_path = '../Zootopia/animals_webpage.html'

    query = input("Enter a name of an animal: ").strip()
    animals = fetch_animals_from_api(query)

    with open(template_path, 'r') as f:
        template_html = f.read()

    if animals:
        cards_html = "\n".join([generate_animal_card(animal) for animal in animals])
    else:
        cards_html = f'<h2>The animal "{query}" doesn\'t exist in our database.</h2>'

    final_html = template_html.replace('<!-- ANIMAL_CARDS_PLACEHOLDER -->', cards_html)

    with open(output_path, 'w') as f:
        f.write(final_html)

    print(f"✅ Website was successfully generated for '{query}' and saved to {output_path}")

if __name__ == '__main__':
    main()


