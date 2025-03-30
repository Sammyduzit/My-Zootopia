import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

animals = []
for entry in animals_data:
    # Create dict container for each animal
    animal_dict = {}

    # Get data for each animal, if no data value will be None
    animal_dict["name"] = entry.get("name")
    animal_dict["diet"] = entry.get("taxonomy", {}).get("order")
    locations = entry.get("locations")
    animal_dict["locations"] = ", ".join(locations)
    animal_dict["type"] = entry.get("characteristics", {}).get("type")

    # Add data to animals list
    animals.append(animal_dict)

for animal in animals:
    for entry in animal:
        if animal[entry]:
            print(f"{entry}: {animal[entry]}")
    print("")
