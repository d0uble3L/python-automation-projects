import json

def update_json_template(input_file, user_updates, output_file):
    """
    Update specific values in a JSON template and save the result to a new file.

    :param input_file: str, path to the input JSON template file
    :param user_updates: dict, dictionary containing the values to update in the JSON template
    :param output_file: str, path to the output JSON file
    """
    # Read the input JSON template file
    with open(input_file, 'r') as file:
        json_data = json.load(file)

    # Recursive function to update nested dictionaries
    def update_dict(d, u):
        for k, v in u.items():
            if isinstance(v, dict) and k in d:
                update_dict(d[k], v)
            else:
                d[k] = v

    # Update the JSON data with user inputs
    update_dict(json_data, user_updates)

    # Write the updated JSON data to the output file
    with open(output_file, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"Updated JSON file saved as {output_file}")

# Example usage
if __name__ == "__main__":
    input_template = 'template.json'
    updates = {
        'name': 'John Doe',
        'age': 30,
        'address': {
            'city': 'New York'
        }
    }
    output_filename = 'updated_template.json'

    update_json_template(input_template, updates, output_filename)
