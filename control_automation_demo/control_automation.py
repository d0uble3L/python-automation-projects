# update_json.py
import json
import random

def control_evidence_logic():
    """Generates random numbers and calculates the percentage."""
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    percent = number1 / number2 * 100
    return percent, number1, number2

def determine_evidence_result(percent):
    """Determines the evidence result based on the percentage."""
    return "SUCCESS" if percent > 95 else "FAILED"

def update_evidence_json_file(file_path, key_path, new_value):
    """Updates a value in a JSON file.

    Args:
        file_path: The path to the JSON file.
        key_path: The dot-separated key path to update.
        new_value: The new value for the key.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        keys = key_path.split('.')
        d = data
        for key in keys[:-1]:
            d = d[key]
        d[keys[-1]] = new_value

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Value for key '{key_path}' in file '{file_path}' updated successfully.")
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error: {e}")

def read_evidence_json_file(file_path):
    """Reads and prints the contents of a JSON file.

    Args:
        file_path: The path to the JSON file.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        # print(json.dumps(data, indent=4))
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    percent, number1, number2 = control_evidence_logic()
    evidence_result_value = determine_evidence_result(percent)

    update_evidence_json_file('control.json', 'evidenceResult', evidence_result_value)
    update_evidence_json_file('control.json', 'evidenceTest.testPercent', percent)
    update_evidence_json_file('control.json', 'evidenceTest.testScanned', number1)
    update_evidence_json_file('control.json', 'evidenceTest.testScope', number2)

    data = read_evidence_json_file('control.json')
    if data:
        evidence_test_details = json.dumps(data['evidenceTest'], separators=(',', ':'))
        update_evidence_json_file('control.json', 'details', evidence_test_details)