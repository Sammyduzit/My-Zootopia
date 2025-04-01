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


def generate_animal_card(animal_data):
    """
    Generate HTML card for a single animal.
    Silently skips any missing or None fields.
    :param animal_data: Dictionary containing animal data
    :return: HTML string with animal card infos
    """
    card = ['<li class="cards__item">']

    if animal_data.name:
        card.append(f'<div class="card__title">{animal_data.name}</div>')

    card.append('<div class="card__text">\n<ul>')

    if animal_data.taxonomy.scientific_name:
        card.append(f'<li><strong>Scientific Name:</strong> {animal_data.taxonomy.scientific_name}</li>')

    if animal_data.characteristics.type:
        card.append(f'<li><strong>Type:</strong> {animal_data.characteristics.type}</li>')

    if animal_data.characteristics.skin_type:
        card.append(f'<li><strong>Skin Type:</strong> {animal_data.characteristics.skin_type}</li>')

    if animal_data.locations:
        card.append(f'<li><strong>Location(s):</strong> {", ".join(animal_data.locations)}</li>')

    if animal_data.characteristics.habitat:
        card.append(f'<li><strong>Habitat:</strong> {animal_data.characteristics.habitat}</li>')

    if animal_data.characteristics.diet:
        card.append(f'<li><strong>Diet:</strong> {animal_data.characteristics.diet}</li>')

    if animal_data.characteristics.main_prey:
        card.append(f'<li><strong>Main Prey:</strong> {animal_data.characteristics.main_prey}</li>')

    if animal_data.characteristics.predators:
        card.append(f'<li><strong>Predators:</strong> {animal_data.characteristics.predators}</li>')

    if animal_data.characteristics.distinctive_feature:
        card.append(f'<li><strong>Distinctive Features:</strong> {animal_data.characteristics.distinctive_feature}</li>')

    if animal_data.characteristics.temperament:
        card.append(f'<li><strong>Temperament:</strong> {animal_data.characteristics.temperament}</li>')

    if animal_data.characteristics.name_of_young:
        card.append(f'<li><strong>Offspring Name:</strong> {animal_data.characteristics.name_of_young}</li>')

    card.append("</ul>")
    card.append("</div>")
    card.append("</li>")
    return "\n".join(card) + "\n"


def generate_all_cards(animals):
    """
    Generate the HTML string for all animals.
    :param animals: List of Animal objects
    :return: String containing HTML markup for all animal cards
    """
    return "".join(generate_animal_card(animal) for animal in animals)


def generate_html_content(user_selection, matching, missing, show_all=False):
    """Generate complete HTML content with sections"""
    html_parts = []

    if show_all:
        html_parts.append('<h2>All Animals</h2>')
        html_parts.extend(generate_animal_card(a) for a in matching)
    elif matching:
        html_parts.append(f'<h2>Matching Animals with {user_selection.capitalize()}</h2>')
        html_parts.extend(generate_animal_card(a) for a in matching)

    if missing:
        html_parts.append('<h2 class="missing-data">Animals with Unspecified Skin Type</h2>')
        html_parts.extend(generate_animal_card(a) for a in missing)

    return ''.join(html_parts)


def insert_data_into_template(template, animals_html):
    """
    Combine template with generated animal HTML.
    :param template: HTML template string
    :param animals_html: Generated animal cards HTML
    :return: Complete HTML page as string
    """
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_html)


def get_unique_skin_types(animals):
    """
    Extract all unique skin_type values from animals data.
    :param animals: List of Animal objects to process
    :return: Set of unique skin_type strings found in the animals data (excluding None or empty values)
    """
    skin_types = set()
    for animal in animals:
        if animal.characteristics.skin_type:
            skin_types.add(animal.characteristics.skin_type)
    return skin_types


def display_skin_types(skin_types):
    """
    Display available skin type options to the user in a numbered list.
    :param skin_types: Set of unique skin_type strings to display
    :return: None
    """
    print("Available skin types:")
    print("0. Show all animals (ignore skin type)")
    for i, skin_type in enumerate(sorted(skin_types), 1):
        print(f"{i}. {skin_type}")


def get_skin_type_by_user(skin_types):
    """
    Prompt user to select a skin type from available options (case-insensitive).
    :param skin_types: Set of available skin types
    :return: The selected skin type or 'all'
    """
    skin_types_lower = {skin.lower(): skin for skin in skin_types}

    while True:
        try:
            choice = input("\nEnter the skin type you want to filter by: ").strip()
            if choice == '0' or choice.lower() == "all":
                user_selection = 'all'
                break
            if choice in skin_types_lower:
                user_selection = choice
                break
            if choice.isdigit() and 0 < int(choice) <= len(skin_types):
                user_selection = sorted(skin_types)[int(choice)-1]
                break
            print("Invalid selection. Please choose from the listed skin types.")
        except (EOFError, KeyboardInterrupt):
            sys.exit("Operation cancelled by user.")
    return user_selection


def filter_animals_by_skin_type(animals, selected_skin_type):
    """
    Separate animals into matching and missing skin type groups.
    :param animals: List of Animal objects to filter
    :param selected_skin_type: String specifying the skin type to filter by
            ('all' will return all animals in first group)
    :return: tuple: (matching_animals, missing_skin_animals) where:
               - matching_animals: List of animals with matching skin_type
               - missing_skin_animals: List of animals with no skin_type data
                                      (empty list when selected_skin_type is 'all')
    """
    matching = []
    missing = []

    if selected_skin_type.lower() == 'all':
        return animals, []

    for animal in animals:
        if not animal.characteristics.skin_type:
            missing.append(animal)
        elif animal.characteristics.skin_type.lower() == selected_skin_type.lower():
            matching.append(animal)

    return matching, missing


def main():
    """
    Main function that orchestrates the program flow:
    1. Load and process animal data
    2. Show available skin types
    3. Get user selection
    4. Filter animals
    5. Generate and save HTML
    """
    # Load and process data
    json_data = load_json_file('animals_data.json')
    animals = process_animal_data(json_data)

    # Display skin types and get user choice
    skin_types = get_unique_skin_types(animals)
    display_skin_types(skin_types)
    user_selection = get_skin_type_by_user(skin_types)

    #Filter animals
    matching, missing = filter_animals_by_skin_type(animals, user_selection)
    print(f"\nFound {len(matching)} matching animal(s)")
    if missing:
        print(f"Plus {len(missing)} animal(s) with unspecified skin type")

    #Generate HTML
    html_template = load_html_template("animals_template.html")
    show_all = user_selection.lower() == 'all'
    animals_html = generate_html_content(user_selection, matching, missing, show_all)
    final_html = insert_data_into_template(html_template, animals_html)

    save_to_file("animals.html", final_html)


if __name__ == "__main__":
    main()