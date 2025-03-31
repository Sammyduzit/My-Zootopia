import json
import sys


def load_data(file_path):
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
                print(f"Error: Invalid JSON format in {file_path}: {e}")
    except FileNotFoundError:
        print(f"Error file not found: {file_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Could not read file {file_path}: {e}")
        sys.exit(1)


def write_data(file_path, data):
    """
    Write a string to a file.
    :param file_path: Path where the file will be written
    :param data: String data to be written to the file
    :return: None
    :raises: SystemExit if file cannot be written
    """
    try:
        with open(file_path, "w") as handle:
            handle.write(data)
    except IOError as e:
        print(f"Error: Could not write to file {file_path}: {e}")
        sys.exit(1)


def load_html(file_path):
    """
    Load and return HTML content.
    :param file_path: Path to the HTML file to be loaded
    :return: String containing the HTML content
    :raises: SystemExit if file not found or cannot be read
    """
    try:
        with open(file_path, "r") as handle:
            return handle.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Could not read HTML template {file_path}: {e}")
        sys.exit(1)


def extract_data(data):
    """
    Extract and format relevant animal data from the raw JSON data.
    :param data: Raw JSON data containing animal information
    :return: List of dictionaries containing formatted animal data
    :raises: SystemExit if input data is not in expected format
    """
    try:
        animals = [
            {
                "name": animal.get("name"),
                "diet": animal.get("characteristics", {}).get("diet"),
                "locations": ", ".join(animal.get("locations", [])),
                "type": animal.get("characteristics", {}).get("type")
            }
            for animal in data
        ]
        return animals
    except (AttributeError, TypeError) as e:
        print(f"Error: Wrong data format: {e}")
        sys.exit()


def serialize_animal(animal_obj):
    """
    Serialize a single animal's data into an HTML list item.
    Silently skips any missing or None fields.
    :param animal_obj: Dictionary containing animal data (name, diet, locations, type)
    :return: String containing HTML markup for the animal card
    """
    output = '<li class="cards__item">\n'

    if animal_obj.get('name'):
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'

    output += '<p class="card__text">\n'

    if animal_obj.get('diet'):
        output += f'<strong>Diet:</strong> {animal_obj["diet"]}<br/>\n'

    if animal_obj.get('locations'):
        output += f'<strong>Location(s):</strong> {animal_obj["locations"]}<br/>\n'

    if animal_obj.get('type'):
        output += f'<strong>Type:</strong> {animal_obj["type"]}<br/>\n'

    output += '</p>\n</li>\n'
    return output


def generate_string(data):
    """
    Generate the HTML string for all animals.
    :param data: Raw JSON data containing all animal information
    :return: String containing HTML markup for all animal cards
    """
    animals = extract_data(data)
    return "".join(serialize_animal(animal) for animal in animals)


def main():
    """
    Main function that orchestrates the program flow:
    1. Loads animal data from JSON file
    2. Loads HTML template
    3. Generates HTML content for animals
    4. Inserts animal content into template
    5. Writes final HTML to output file
    """
    animals_data = load_data('animals_data.json')
    html_data = load_html("animals_template.html")
    animals_string = generate_string(animals_data)
    new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    write_data("animals.html", new_html_data)


if __name__ == "__main__":
    main()