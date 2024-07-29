# Update Values in a JSON File with Python

## Installation
There are no additional dependencies needed besides Python itself.

## Usage
1. Save the following code as a Python script (e.g., `update_json.py`).
2. Modify the `file_path`, `key_to_update`, and `new_value` variables at the bottom according to your needs.
3. Run the script: `python update_json.py`

### Example:
```python
import json

def update_json_file(file_path, key, new_value):
    """Updates a value in a JSON file.

    Args:
        file_path: The path to the JSON file.
        key: The key to update.
        new_value: The new value for the key.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        data[key] = new_value

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Value for key '{key}' updated successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{file_path}'.")

# Example usage
file_path = 'data.json'
key_to_update = 'name'
new_value = 'New Name'

update_json_file(file_path, key_to_update, new_value)
