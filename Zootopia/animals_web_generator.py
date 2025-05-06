import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_card(animal):
    """Generates HTML for a single animal card with more info."""
    parts = []
    name = animal.get('name')
    taxonomy = animal.get('taxonomy', {})
    characteristics = animal.get('characteristics', {})
    locations = animal.get('locations')

    # Basic Info
    if name:
        parts.append(f"<h2>{name}</h2>")
    if 'scientific_name' in taxonomy:
        parts.append(f"<p><strong>Scientific Name:</strong> {taxonomy['scientific_name']}</p>")
    if locations and len(locations) > 0:
        parts.append(f"<p><strong>Location:</strong> {', '.join(locations)}</p>")
    if 'diet' in characteristics:
        parts.append(f"<p><strong>Diet:</strong> {characteristics['diet']}</p>")
    if 'type' in characteristics:
        parts.append(f"<p><strong>Type:</strong> {characteristics['type']}</p>")

    # More Details
    optional_fields = [
        ('slogan', 'Slogan'),
        ('lifespan', 'Lifespan'),
        ('color', 'Color'),
        ('habitat', 'Habitat'),
        ('weight', 'Weight'),
        ('top_speed', 'Top Speed'),
        ('temperament', 'Temperament'),
        ('predators', 'Predators'),
        ('group_behavior', 'Group Behavior')
    ]
    for field_key, field_label in optional_fields:
        if field_key in characteristics:
            parts.append(f"<p><strong>{field_label}:</strong> {characteristics[field_key]}</p>")

    return f'<li class="cards__item">\n' + "\n".join(parts) + '\n</li>'

def main():
    # Dateien laden
    data_path = 'animals_data.json'  # Passe den Namen ggf. an
    template_path = 'animals_template.html'
    output_path = 'animals_webpage.html'

    # Daten & Template lesen
    animals = load_data(data_path)
    with open(template_path, 'r') as f:
        template_html = f.read()

    # Tier-Karten bauen
    cards_html = "\n".join([generate_animal_card(animal) for animal in animals])

    # Platzhalter ersetzen
    if '<!-- ANIMAL_CARDS_PLACEHOLDER -->' in template_html:
        final_html = template_html.replace('<!-- ANIMAL_CARDS_PLACEHOLDER -->', cards_html)
        print(f"✅ {len(animals)} Tiere geladen & Platzhalter ersetzt.")
    else:
        print("⚠️ Platzhalter wurde NICHT gefunden! Bitte prüfe das Template.")
        return

    # HTML-Datei schreiben
    with open(output_path, 'w') as f:
        f.write(final_html)

    print(f"✅ HTML-Seite wurde erfolgreich erstellt: {output_path}")

if __name__ == '__main__':
    main()


