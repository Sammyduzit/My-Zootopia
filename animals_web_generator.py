import json
import sys
from dataclasses import dataclass, field

@dataclass
class Taxonomy:
    kingdom: str = None
    phylum: str = None
    class_name: str = None  # 'class' is a reserved keyword in Python.
    order: str = None
    family: str = None
    genus: str = None
    scientific_name: str = None

@dataclass
class Characteristics:
    distinctive_feature: str = None
    temperament: str = None
    training: str = None
    diet: str = None
    average_litter_size: str = None
    type: str = None
    common_name: str = None
    slogan: str = None
    group: str = None
    color: str = None
    skin_type: str = None
    lifespan: str = None
    main_prey: str = None
    name_of_young: str = None
    habitat: str = None
    predators: str = None
    lifestyle: str = None
    favorite_food: str = None
    top_speed: str = None
    weight: str = None
    length: str = None

@dataclass
class Animal:
    """Complete animal data structure with taxonomy and characteristics."""
    name: str = None
    taxonomy: Taxonomy = field(default_factory=Taxonomy)
    locations: list = field(default_factory=list)
    characteristics: Characteristics = field(default_factory=Characteristics)


def load_json_file(file_path):
    """
    Load and return data from a JSON file.
    :param file_path: Path to the JSON file to be loaded
    :return: Dictionary containing the parsed JSON data
    :raises: SystemExit if file not found or JSON decode error occurs
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            try:
                return json.load(handle)
            except json.JSONDecodeError as e:
                sys.exit(f" Invalid JSON format in {file_path}: {e}")
    except FileNotFoundError:
        sys.exit(f"File not found: {file_path}")
    except IOError as e:
        sys.exit(f"Error: Could not read file {file_path}: {e}")


def save_to_file(file_path, content):
    """
    Write content to a file.
    :param file_path: File path destination
    :param content: String content to be written to the file
    :return: None
    :raises: SystemExit if file cannot be written
    """
    try:
        with open(file_path, "w", encoding="utf-8") as handle:
            handle.write(content)
    except IOError as e:
        sys.exit(f"Error: Could not write to file {file_path}: {e}")


def load_html_template(file_path):
    """
    Load and return HTML template content.
    :param file_path: Path to the HTML file to be loaded
    :return: HTML content as string
    :raises: SystemExit if file not found or cannot be loaded
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return handle.read()
    except FileNotFoundError:
        sys.exit(f"Error: File not found: {file_path}")
    except IOError as e:
        sys.exit(f"Error: Could not read HTML template {file_path}: {e}")


def create_animal_instance(animal_data):
    """
    Create an Animal instance from raw JSON data.
    :param animal_data: Dictionary containing animal data
    :return: Structured Animal object with all data
    """
    taxonomy_data = animal_data.get("taxonomy", {})
    characteristics_data = animal_data.get("characteristics", {})

    taxonomy = Taxonomy(
        kingdom=taxonomy_data.get("kingdom"),
        phylum=taxonomy_data.get("phylum"),
        class_name=taxonomy_data.get("class"),
        order=taxonomy_data.get("order"),
        family=taxonomy_data.get("family"),
        genus=taxonomy_data.get("genus"),
        scientific_name=taxonomy_data.get("scientific_name"),
    )

    characteristics = Characteristics(
        distinctive_feature=characteristics_data.get("distinctive_feature"),
        temperament=characteristics_data.get("temperament"),
        training=characteristics_data.get("training"),
        diet=characteristics_data.get("diet"),
        average_litter_size=characteristics_data.get("average_litter_size"),
        type=characteristics_data.get("type"),
        common_name=characteristics_data.get("common_name"),
        slogan=characteristics_data.get("slogan"),
        group=characteristics_data.get("group"),
        color=characteristics_data.get("color"),
        skin_type=characteristics_data.get("skin_type"),
        lifespan=characteristics_data.get("lifespan"),
        main_prey=characteristics_data.get("main_prey"),
        name_of_young=characteristics_data.get("name_of_young"),
        habitat=characteristics_data.get("habitat"),
        predators=characteristics_data.get("predators"),
        lifestyle=characteristics_data.get("lifestyle"),
        favorite_food=characteristics_data.get("favorite_food"),
        top_speed=characteristics_data.get("top_speed"),
        weight=characteristics_data.get("weight"),
        length=characteristics_data.get("length"),
    )

    return Animal(
        name=animal_data.get("name"),
        taxonomy=taxonomy,
        locations=animal_data.get("locations", []),
        characteristics=characteristics,
    )


def process_animal_data(animals_json_data):
    """
    Convert raw animal data into structured Animal objects.
    :param animals_json_data: List of animal dictionaries from JSON
    :return:
    """
    animals = []
    for animal_data in animals_json_data:
        try:
            animal = create_animal_instance(animal_data)
            animals.append(animal)
        except Exception as e:
            print(f"Error parsing animal data: {e}")
    return animals


def generate_animal_card(animal_obj):
    """
    Generate HTML card for a single animal.
    Silently skips any missing or None fields.
    :param animal_obj: Dictionary containing animal data
    :return: HTML string with animal card infos
    """
    card = ['<li class="cards__item">']

    if animal_obj.name:
        card.append(f'<div class="card__title">{animal_obj.name}</div>')

    card.append('<p class="card__text">')

    if animal_obj.characteristics.diet:
        card.append(f'<strong>Diet:</strong> {animal_obj.characteristics.diet}<br/>')

    if animal_obj.locations:
        card.append(f'<strong>Location(s):</strong> {", ".join(animal_obj.locations)}<br/>')

    if animal_obj.characteristics.type:
        card.append(f'<strong>Type:</strong> {animal_obj.characteristics.type}<br/>')

    card.append("</p>")
    card.append("</li>")
    return "\n".join(card) + "\n"


def generate_all_cards(animals):
    """
    Generate the HTML string for all animals.
    :param animals: List of Animal objects
    :return: String containing HTML markup for all animal cards
    """
    return "".join(generate_animal_card(animal) for animal in animals)


def insert_into_template(template, animals_html):
    """
    Combine template with generated animal HTML.
    :param template: HTML template string
    :param animals_html: Generated animal cards HTML
    :return: Complete HTML page as string
    """
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_html)


def main():
    """
    Main function that orchestrates the program flow:
    1. Load raw animal data
    2. Process into structured objects
    3. Load HTML template
    4. Generate animal cards HTML
    5. Combine with template
    6. Save final output
    """
    json_data = load_json_file('animals_data.json')
    animals = process_animal_data(json_data)
    html_template = load_html_template("animals_template.html")
    animals_html = generate_all_cards(animals)
    final_html = insert_into_template(html_template, animals_html)
    save_to_file("animals.html", final_html)


if __name__ == "__main__":
    main()