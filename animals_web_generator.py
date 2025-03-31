import json


def load_data(file_path):
    """
    Load and return data from a JSON file.
    :param file_path: Path to the JSON file to be loaded
    :return: Dictionary containing the parsed JSON data
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def write_data(file_path, data):
    """
    Write a string to a file.
    :param file_path: Path where the file will be written
    :param data: String data to be written to the file
    :return: None
    """
    with open(file_path, "w") as handle:
        handle.write(data)


def load_html(file):
    """
    Load and return HTML content.
    :param file: Path to the HTML file to be loaded
    :return: String containing the HTML content
    """
    with open(file, "r") as handle:
        return handle.read()


def extract_data(data):
    """
    Extract and format relevant animal data from the raw JSON data.
    :param data: Raw JSON data containing animal information
    :return: List of dictionaries containing formatted animal data
    """
    animals = [
        {
            "name": animal.get("name"),
            "diet": animal.get("taxonomy", {}).get("order"),
            "locations": ", ".join(animal.get("locations", [])),
            "type": animal.get("characteristics", {}).get("type")
        }
        for animal in data
    ]
    return animals


def serialize_animal(animal_obj):
    """
    Serialize a single animal's data into an HTML list item.
    :param animal_obj: Dictionary containing animal data (name, diet, locations, type)
    :return: String containing HTML markup for the animal card
    """
    # define an empty string
    output = ''
    # append information to each string
    output += "<li class='cards__item'>\n"
    output += f"<div class='card__title'> {animal_obj['name']} </div>\n"
    output += "<p class='card__text'>\n"
    output += f"<strong> Diet: </strong> {animal_obj['diet']} <br/>\n"
    output += f"<strong> Location(s): </strong> {animal_obj['locations']} <br/>\n"
    if animal_obj['type']:
        output += f"<strong> Type: </strong> {animal_obj['type']} <br/>\n"
    output += "</p>\n</li>\n"

    return output


def generate_string(data):
    """
    Generate the HTML string for all animals.
    :param data: Raw JSON data containing all animal information
    :return: String containing HTML markup for all animal cards
    """
    output = ''  # define an empty string
    animals = extract_data(data)

    for animal in animals:
        output += serialize_animal(animal)

    return output


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