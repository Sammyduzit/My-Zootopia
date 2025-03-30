import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def write_data(file_path, data):
    with open(file_path, "w") as handle:
        handle.write(data)

animals_data = load_data('animals_data.json')

def extract_data(data):
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


def load_html(file):
    with open(file, "r") as handle:
        return handle.read()

html_data = load_html("animals_template.html")

def generate_string(data):
    output = ''  # define an empty string
    animals = extract_data(data)

    for animal in animals:
        # append information to each string
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['diet']}\n"
        output += f"Location(s): {animal['locations']}\n"
        if animal['type']:
            output += f"Type: {animal['type']}\n"
        output += "\n"

    return output


# def replace_infos(file, to_replace, replacement):
#     return file.replace(to_replace, replacement)


animals_string = generate_string(animals_data)

new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_string)


write_data("animals.html", new_html_data)