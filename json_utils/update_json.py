# update_json.py
import json
import random

def generateNumbers():
  # Generate two random integers between 1 and 100 (inclusive)
  number1 = random.randint(1, 100)
  number2 = random.randint(1, 100)
  percent = number1 / number2 * 100

  return percent

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

    print(f"Value for key '{key}' in file '{file_path}' updated successfully.")
  except FileNotFoundError:
    print(f"File '{file_path}' not found.")
  except json.JSONDecodeError:
    print(f"Error decoding JSON in file '{file_path}'.")

def generate_evidenceresultValue(percent):
  # Check if the percentage is less than 95%
  if percent > 95:
      evidenceResultValue = "SUCCESS"
  else:
    evidenceResultValue = "FAILED"

  return evidenceResultValue
  

if __name__ == "__main__":
  percent  = generateNumbers()
  evidenceResultValue = generate_evidenceresultValue(percent)
  update_json_file('control.json','evidenceResult', evidenceResultValue)
  print(percent, evidenceResultValue)


# # Example usage
# file_path = 'data.json'
# key_to_update = 'name'
# new_value = 'New Name'
# update_json_file(file_path, key_to_update, new_value)
