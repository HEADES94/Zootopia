import data_fetcher  # ✅ das neue Modul importieren


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

    # ✅ Tiername vom Nutzer abfragen
    animal_name = input("Please enter an animal: ").strip()

    # ✅ Daten holen aus dem neuen Modul
    animals = data_fetcher.fetch_data(animal_name)

    # Template lesen
    with open(template_path, 'r') as f:
        template_html = f.read()

    # Karten bauen ODER Fehlermeldung
    if animals:
        cards_html = "\n".join([generate_animal_card(animal) for animal in animals])
    else:
        cards_html = f'<h2>The animal "{animal_name}" doesn\'t exist in our database.</h2>'

    # Platzhalter ersetzen
    final_html = template_html.replace('<!-- ANIMAL_CARDS_PLACEHOLDER -->', cards_html)

    # Seite schreiben
    with open(output_path, 'w') as f:
        f.write(final_html)

    print(f"✅ Website was successfully generated for '{animal_name}' and saved to {output_path}")


if __name__ == '__main__':
    main()


