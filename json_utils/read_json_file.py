import json

def read_json_file(file_path):
    """Reads and prints the contents of a JSON file.

    Args:
        file_path: The path to the JSON file.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{file_path}'.")

# Example usage
file_path = 'data.json'
read_json_file(file_path)
