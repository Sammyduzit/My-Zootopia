import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

def display_data():
    animals = [
        {
            "name": entry.get("name"),
            "diet": entry.get("taxonomy", {}).get("order"),
            "locations": ", ".join(entry.get("locations", [])),
            "type": entry.get("characteristics", {}).get("type")
        }
        for entry in animals_data
    ]

    for animal in animals:
        for entry in animal:
            if animal[entry]:
                print(f"{entry}: {animal[entry]}")
        print("")


display_data()